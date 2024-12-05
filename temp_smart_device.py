from sense_hat import SenseHat

# a function that reads the temperature from the sensors on rasp pi
# the temp is adjusted to have a reading similiar to my thermostat.
#This function can be imprted elsewhere

def get_temp():
    sense = SenseHat()
    sense.clear()
    #sense.clear(255,255,255)
    temp = sense.get_temperature()
    adjusted_temp = round(temp - 14.5, 2)
    
    if adjusted_temp <= 16:
        sense.show_message("Temp Cold", text_colour = (0,0,255))
        print(f"Temp is {adjusted_temp}")
    elif adjusted_temp <= 23:
        sense.show_message("good",text_colour = (0,255,0))
        print(f"Temp is {adjusted_temp}") 
    else :
        sense.show_message("too hot", text_colour = (255,0,0) )
        print(f"Temp is {adjusted_temp}")
  
if __name__ == "__main__":
    get_temp()
 
