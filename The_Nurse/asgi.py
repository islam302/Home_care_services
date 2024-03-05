<<<<<<< HEAD
import os
=======
"""
ASGI config for The_Nurse project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

>>>>>>> 05164f650db4f2cdf19ab5c27efadd7118f6d4de
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'The_Nurse.settings')

application = get_asgi_application()
