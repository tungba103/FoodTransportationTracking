import time
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from humidity.models import Humidity
from transport.models import Transport

while True:
    try:
        latest_humidity = Humidity.objects.latest('timestamp')
        freezer = Transport.objects.latest('id')
        print(latest_humidity.value, freezer.delta_humidity, freezer.default_humidity)
        if latest_humidity.value - freezer.delta_humidity > freezer.default_humidity:
            freezer.freezer_status = freezer.freezer_status + 1
            print(f"Freezer status: {freezer.freezer_status}")
        else :
            freezer.freezer_status = freezer.freezer_status - 1
            print(f"Freezer status: {freezer.freezer_status}")
        freezer.save()
    except Humidity.DoesNotExist:
        pass

    time.sleep(1)
