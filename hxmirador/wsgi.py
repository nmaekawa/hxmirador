"""
WSGI config for hxmirador project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from dotenv import load_dotenv

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hxmirador.settings.prod")

# if dotenv file, load it
dotenv_path = os.environ.get(
    'HXMIRADOR_DOTENV_PATH', 'hxmirador.settings.prod')
if dotenv_path:
    load_dotenv(dotenv_path=dotenv_path, override=True)

application = get_wsgi_application()
