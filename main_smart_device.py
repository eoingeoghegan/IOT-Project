#from accel_smart_device import sudden_fall

from button_alert_smart_device import button_detect
from humidity_smart_device import get_humidity
from smart_device_data import smart_device_data
from take_photo import capture_image
from temp_smart_device import get_temp
from sense_hat import SenseHat
from time import sleep



# Initialize Sense HAT
sense = SenseHat()
while True:
     
    get_temp()

    
    






