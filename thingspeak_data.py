from sense_hat import SenseHat
import requests
import time
from take_photo import capture_image
#for uploading image to glitch
import os
import json
#for using Blynk
import BlynkLib

sense = SenseHat()

#Blynk authentication token and Created an instance of Blynk
BLYNK_AUTH_TOKEN = "6JwZ0zMXTepx2ElsQJrPAjot77d8iu7a"
blynk = BlynkLib.Blynk(BLYNK_AUTH_TOKEN)



# Glitch URL path and path where images are saved on rasp Pi
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
    

#Thingspeak Keys to communicating data to thinspeak graphs

THINGSPEAK_WRITE_API_KEY = "YVJGVZM4E13M0CLF"
THINGSPEAK_CHANNEL_URL = "https://api.thingspeak.com/update"

#This function sends temp, humidity and values for xyz to thingspeak to diffenrent fields. 
#The fields store the info in the form of graphs
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
   


#Handler for the virtual pins controlling the datastreams
#This handles the button with a datastream using 1 and 0. If the position of the button is at 0 then it turns off the device nd 1 turns it on.
@blynk.on("V0")
def hadnle_V0_write(value):
    button_value= value[0]
    print(f"Current button value: {button_value}")
    if button_value == '1':
       print ("Switch is on")
       sense.clear(255,255,255)
    else:
        print("Switch is off")
        sense.clear()
    print("testing value 1 for on, 0 for off{value}")
# blynk.run() only works for me when at the beginning of the loop, it connects to the blynk webiste and allows the handle for the button to be used.
#It needed a try / except to allow the code to execute properly. Otherwise the code ran but the handler wouldnt work.
# loop to send the data continuously to the thingspeak every 15 seconds.
#Its checking the temp, humidity and accel sensors on rasp pi and sending them to thingspeak every 15 seconds
#Its also checking to see if the accel moves faster than 2, if so it knows fall is true which then waits 5 seconds, takes a photo and uploads it to glitch.
#The loop restarts then.
fall_detection = 2
try:
    while True:
        temperature = round(sense.get_temperature(),2)
        adjusted_temp = temperature - 15
        blynk.run()
        blynk.virtual_write(1, adjusted_temp)
        blynk.virtual_write(2, sense.humidity)
        
        
        
        humidity = round(sense.get_humidity(),2)
        accel = sense.get_accelerometer_raw()
        x= round(accel['x'],2) 
        y= round(accel['y'],2)
        z= round(accel['z'],2)

        print(f"Sending Temperature: {adjusted_temp}C, Humidity : {humidity}% and Accel Values: {x}, {y}, {z}")
        send_to_thingspeak(adjusted_temp, humidity, x, y, z)
        
        fall=False
        if x > fall_detection or y > fall_detection or z > fall_detection:
            fall = True
            print("Fall detected! Picture in 5 seconds")
            time.sleep(5)
            print("Taking picture now and uploading to glitch")
            capture_image(image_path)
            upload_image(image_path)
            result = upload_image(image_path)
            blynk.set_property(3,"urls",result)

        time.sleep(15)
except KeyboardInterrupt:  
        print("exiting")