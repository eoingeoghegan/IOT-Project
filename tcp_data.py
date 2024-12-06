from smart_device_data import smart_device_data
from sense_hat import SenseHat
from time import sleep

deviceID = "Smart Care Device"

sense = SenseHat()

while True: 
    device_readings = smart_device_data(deviceID)
    readings = str(device_readings)
    print(readings)
    sleep(2)
    
    






