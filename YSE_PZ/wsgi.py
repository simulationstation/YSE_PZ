"""
WSGI config for YSE_PZ project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import sys
sys.stdout = sys.__stdout__
sys.stderr = sys.__stderr__

import os

from django.core.wsgi import get_wsgi_application

from configparser import RawConfigParser
from YSE_PZ.settings_utils import settings_file_path

configFile = settings_file_path(__file__)

config = RawConfigParser()
config.read(configFile)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "YSE_PZ.settings")

application = get_wsgi_application()
