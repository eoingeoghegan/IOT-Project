from sense_hat import SenseHat
import requests
import time


sense = SenseHat()

# ThingSpeak API Key and URL
THINGSPEAK_WRITE_API_KEY = "YVJGVZM4E13M0CLF"
THINGSPEAK_CHANNEL_URL = "https://api.thingspeak.com/update"

# temp and humidity variable to use when sending to thingspeak. temp changed to adjusted_temp for realistic readings.
#both rounded to two decimal places
temperature = round(sense.get_temperature(),2)
adjusted_temp = temperature - 15
humidity = round(sense.get_humidity(),2)

# This is the function that that will send the payload consisting of temp an humidity to the two graphs for visualisation
def send_to_thingspeak(adjusted_temp, humidity ):
    payload = {
        'api_key': THINGSPEAK_WRITE_API_KEY,
        'field1': adjusted_temp,
        'field2': humidity  
    }

    # this will request the URL and attempt to deliver the payload, if successful code will = 200 or else give a unsuccessful code  
    response = requests.get(THINGSPEAK_CHANNEL_URL, params=payload)

    if response.status_code == 200:
        print("Data sent to ThingSpeak.")
    else:
        print(f"Failed to send data. Status code: {response.status_code}")
   


# loop to send the data continuously to the thingspeak every 15 seconds
while True:
    print(f"Temperature: {adjusted_temp} C")
    print(f"humidity {humidity} %")
    send_to_thingspeak(adjusted_temp, humidity)
    
    time.sleep(15)