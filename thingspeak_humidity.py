from sense_hat import SenseHat
import requests
import time

sense = SenseHat()

# ThingSpeak settings
THINGSPEAK_WRITE_API_KEY = "YVJGVZM4E13M0CLF"
THINGSPEAK_CHANNEL_URL = "https://api.thingspeak.com/update"

# Function to send data to ThingSpeak
def send_to_thingspeak(humidity ):
    payload = {
        'api_key': THINGSPEAK_WRITE_API_KEY,
        'field2': humidity,
        
    }
  
    response = requests.get(THINGSPEAK_CHANNEL_URL, params=payload)

    if response.status_code == 200:
        print("Data sent to ThingSpeak.")
    else:
        print(f"Failed to send data. Status code: {response.status_code}")
   


while True:
   
   
    humidity = round(sense.get_humidity(),2)
    print(f"humidity : {humidity} %")
    send_to_thingspeak(humidity)
    # Wait before the next reading (ThingSpeak recommends 15-second intervals for free accounts)
    time.sleep(15)