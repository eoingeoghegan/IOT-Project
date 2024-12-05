from sense_hat import SenseHat
from time import sleep
from temp_smart_device import get_temp 


#this function will allow the sensor to read the humidity, i rounded the humidity as a variable to 2 places.
#if its below 29% it will say air is dry on sense, below 50% = good and above 50% = wet 
def get_humidity():       
    sense = SenseHat()
    sense.clear()
    humidity = sense.get_humidity()
    rounded_humidity = round(humidity,2)

    if humidity < 29:
       sense.show_message("Air is Dry", text_colour = (0,0,255))
       print(f"Humidity: {rounded_humidity} %")
    elif humidity <= 50:
       sense.show_message("Good", text_colour = (0,255,0))
       print(f"Humidity: {rounded_humidity} %") 
    else:
       sense.show_message("Wet", text_colour = (255,0,0))
       print(f"Humidity: {rounded_humidity} %") 


       
if __name__ == "__main__":
        get_humidity()
    