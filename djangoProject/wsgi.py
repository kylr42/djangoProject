"""
WSGI config for djangoProject project.

It exposes the WSGI callable as a module-level variable named ``application``.
https://vk.com/@hacker_timcore-19-uyazvimost-sql-injection-stored-user-agent
For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProject.settings')

application = get_wsgi_application()
