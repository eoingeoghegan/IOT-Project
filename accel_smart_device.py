#imported senseHat allows sensors to be used
from sense_hat import SenseHat 
import time
sense = SenseHat()

# Variables used throughout the script
green = (0,255,0)
red = (255,0,0)

# Set to 5, realistic if movement is faster than this
fall_detection = 5

# function creates sensor varibales and determines if the sensor moves faster than 5, if so it returns fall as true.
def sudden_fall():
    fall=False  
    accel = sense.get_accelerometer_raw()
    x= (accel['x']) 
    y= (accel['y'])
    z= (accel['z'])

    if x > fall_detection or y > fall_detection or z > fall_detection:
        fall = True 
    return fall

#TEST if sudden movement, hat turns red for 1 second, and shows "Fall", then returns to gree
while True:
    if sudden_fall():   #call code for sudden fall
        print("SUDDEN MOVEMENT DETECTED")
        sense.clear(red)
        time.sleep(1)
        sense.show_message("FALL!!", text_colour= [0,0,255], scroll_speed = 0.1)
        sense.clear(green)


    if __name__ == "__main__":
          sudden_fall()