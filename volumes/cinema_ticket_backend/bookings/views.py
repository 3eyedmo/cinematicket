from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema

from movies.models import Schedule
from bookings.models import Booking
from bookings.serializers import BookingSerializer, SeatAvailabilitySerializer, BookingSchema
from bookings.utils import SeatGenerator, SeatStatusUpdater


class SeatAvailabilityView(APIView):
    def get(self, request, schedule_id):
        try:
            schedule = Schedule.objects.select_related("movie", "room").get(
                pk=schedule_id
            )
            bookings = Booking.objects.filter(schedule=schedule).select_related("user")

            seats = SeatGenerator.generate_seat_layout(schedule.room.seats)
            updated_seats = SeatStatusUpdater.mark_booked_seats(
                seats, bookings, request.user
            )

            data = {
                "movie": schedule.movie,
                "schedule": schedule,
                "seats": updated_seats,
            }

            serializer = SeatAvailabilitySerializer(data, context={"request": request})
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)

        except Schedule.DoesNotExist:
            return Response(
                {"error": "Schedule not found"}, status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


@extend_schema(request=BookingSchema)
class BookSeatView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = BookingSerializer(data=request.data, context={"request": request})

        if not serializer.is_valid():
            return Response(
                {"success": False, "errors": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            # Get the schedule instance
            schedule = Schedule.objects.get(pk=request.data["schedule"])
        except Schedule.DoesNotExist:
            return Response(
                {"success": False, "errors": {"schedule": "Invalid schedule ID"}},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Add schedule to validated data
        validated_data = serializer.validated_data
        validated_data["schedule"] = schedule

        # Create the booking
        booking = serializer.create(validated_data)
        return Response(
            {
                "success": True,
                "booking_id": booking.id,
                "seat_number": booking.seat_number,
                "schedule_id": booking.schedule_id,
                "booked_at": booking.booked_at,
            },
            status=status.HTTP_201_CREATED,
        )
