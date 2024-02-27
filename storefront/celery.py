import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'storefront.settings.dev') #setting up the environment variable

celery = Celery('storefront')  #creating an instance of celery
celery.config_from_object('django.conf:settings', namespace='CELERY') #configuring the variables
celery.autodiscover_tasks() #Auto discovering the tasks

# We need to import this module in the init module otherwise python wont see this code