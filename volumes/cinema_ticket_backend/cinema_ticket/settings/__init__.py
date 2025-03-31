import os
if os.getenv('ENVIRONMENT') == 'production':
    from .production import *
else:
    from .development import *