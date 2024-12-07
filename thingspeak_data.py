from sense_hat import SenseHat
import requests
import time
from take_photo import capture_image
#for uploading image to glitch
import os
import json

sense = SenseHat()



GLITCH_API_URL = "https://iot-eoingeoghegan.glitch.me/upload"  
image_path = "/home/egghead1004/images/smart_device.jpg"

#function for uploading an image to glitch thats saved in the image_path. Mine is /home/egghead1004/images/smart_device.jpg
#It check if the image path exists, opens the file and does a post request to glitch with the file where it is stored.

def upload_image(image_path):
    if os.path.exists(image_path):
        with open(image_path, 'rb') as img_file:
            response = requests.post(GLITCH_API_URL, files={'file': img_file})
            print(response)
            httpBody=json.loads(response.text)
            return httpBody["url"]
    else:
        return json.loads(f'{{"message":"Image not found: {image_path}" }}')
    


THINGSPEAK_WRITE_API_KEY = "YVJGVZM4E13M0CLF"
THINGSPEAK_CHANNEL_URL = "https://api.thingspeak.com/update"

# This is the function that that wil two graphs for visualisation
def send_to_thingspeak(adjusted_temp, humidity, x, y, z ):
    payload = {
        'api_key': THINGSPEAK_WRITE_API_KEY,
        'field1': adjusted_temp,
        'field2': humidity,
        'field3': x, 
        'field4': y,
        'field5': z        
    }

    # this will request the URL and attempt to deliver the payload, if successful code will = 200 or else give a unsuccessful code  
    response = requests.get(THINGSPEAK_CHANNEL_URL, params=payload)

    if response.status_code == 200:
        print("Data sent to ThingSpeak.")
    else:
        print(f"Failed to send data. Status code: {response.status_code}")
   


# loop to send the data continuously to the thingspeak every 15 seconds
while True:
    fall_detection =3
    temperature = round(sense.get_temperature(),2)
    adjusted_temp = temperature - 15
    humidity = round(sense.get_humidity(),2)
    accel = sense.get_accelerometer_raw()
    x= round(accel['x'],2) 
    y= round(accel['y'],2)
    z= round(accel['z'],2)

    print(f"Sending Temperature: {adjusted_temp}C, Humidity : {humidity}% and Accel Values {x}, {y}, {z}")
    send_to_thingspeak(adjusted_temp, humidity, x, y, z)
    
    fall=False
    if x > fall_detection or y > fall_detection or z > fall_detection:
        fall = True
        print("Fall detected! Picture in 5 seconds")
        time.sleep(5)
        print("Taking picture now and uploading to glitch")
        capture_image(image_path)
        upload_image(image_path)
    
    time.sleep(15)