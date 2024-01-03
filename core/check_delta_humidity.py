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
        nebulizer = Transport.objects.latest('id')
        print(latest_humidity.value, nebulizer.delta_humidity, nebulizer.default_humidity, nebulizer.nebulizer_status)
        if latest_humidity.value > nebulizer.default_humidity and latest_humidity.value - nebulizer.default_humidity > nebulizer.delta_humidity and nebulizer.nebulizer_status == True:
            nebulizer.nebulizer_status = False
            print(f"nebulizer status: {nebulizer.nebulizer_status}")
        elif latest_humidity.value < nebulizer.default_humidity and nebulizer.default_humidity - latest_humidity.value > nebulizer.delta_humidity and nebulizer.nebulizer_status == False :
            nebulizer.nebulizer_status = True
            print(f"nebulizer status: {nebulizer.nebulizer_status}")
        nebulizer.save()
    except Humidity.DoesNotExist:
        pass

    time.sleep(1)
