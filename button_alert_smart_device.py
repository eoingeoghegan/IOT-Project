from sense_hat import SenseHat
from time import sleep
sense = SenseHat()

# This function activates if the button is pressed, it is an event that is listening in another function below. 
#When button is pressed it will flash red and blue. Can probably take out the second of each colour.
def button_pressed(event):
    if event.action == "pressed":
        sense.show_message("Emergency Button Activated", scroll_speed= 0.05, text_colour= (255,0,0))
        print("Emergency, Alert humans")
        sense.clear(255,0,0)
        sleep(1)
        sense.clear(0,0,255)
        sleep(1)
        sense.clear(255,0,0)
        sleep(1)
        sense.clear(0,0,255)
        sleep(1)

# this function conects the two functions together and is waiting for the button to be pressed.
#when its pressed the event is activated
def button_detect():
        sense.stick.direction_middle = button_pressed  
        print("Press Sensehat button for emergency")
        while True:
            pass



if __name__ == "__main__":
    button_detect()