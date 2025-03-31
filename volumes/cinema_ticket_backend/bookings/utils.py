from typing import List, Dict
from django.contrib.auth import get_user_model
from dataclasses import dataclass
from typing import List, Dict


User = get_user_model()


class SeatGenerator:
    @staticmethod
    def generate_seat_layout(total_seats: int) -> List[Dict]:
        seats = []
        current_row = "A"
        seat_number = 1

        while seat_number <= total_seats:
            for seat_in_row in range(1, 11):
                if seat_number > total_seats:
                    break
                seats.append(
                    {
                        "name": f"{current_row}{seat_in_row}",
                        "number": seat_number,
                        "is_booked": False,
                        "is_booked_by_you": False,
                    }
                )
                seat_number += 1
            current_row = chr(ord(current_row) + 1)
        return seats


class SeatStatusUpdater:
    @staticmethod
    def mark_booked_seats(seats: List[Dict], bookings: List, user) -> List[Dict]:
        booked_seats = {booking.seat_number: booking.user for booking in bookings}

        for seat in seats:
            if seat["name"] in booked_seats:
                seat["is_booked"] = True
                if (
                    user
                    and user.is_authenticated
                    and booked_seats[seat["name"]] == user
                ):
                    seat["is_booked_by_you"] = True
        return seats
