import time
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from temperature.models import Temperature
from transport.models import Transport

while True:
    try:
        latest_temperature = Temperature.objects.latest('timestamp')
        freezer = Transport.objects.latest('id')
        print(latest_temperature.value, freezer.delta_temperature, freezer.default_temperature, freezer.freezer_status)
        if latest_temperature.value > freezer.default_temperature and latest_temperature.value - freezer.default_temperature > freezer.delta_temperature and freezer.freezer_status < 20:
            freezer.freezer_status = freezer.freezer_status + 1
            print(f"Freezer status: {freezer.freezer_status}")
        elif latest_temperature.value < freezer.delta_temperature and freezer.default_temperature - latest_temperature.value > freezer.delta_temperature and freezer.freezer_status > 0:
            freezer.freezer_status = freezer.freezer_status - 1
            print(f"Freezer status: {freezer.freezer_status}")
        freezer.save()
    except Temperature.DoesNotExist:
        pass

    time.sleep(1)
