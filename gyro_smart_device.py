from sense_hat import SenseHat
import time

GREEN = (0, 255, 0)  # RGB for green
RED = (255, 0, 0)    # RGB for red

# Initialise Sense HAT
sense = SenseHat()

# Define threshold for detecting a 90-degree rotation
ROTATION_THRESHOLD = 85  # Degrees (close to 90 for tolerance)

# Start with green LEDs
sense.clear(GREEN)  # Set LEDs to green

# Function to check if the Sense HAT has rotated 90 degrees
def detect_rotation():
    orientation = sense.get_orientation()
    pitch = orientation['pitch']
    roll = orientation['roll']
    yaw = orientation['yaw']
    
  
    # Check if any of the angles is approximately 90 degrees
    if (ROTATION_THRESHOLD <= pitch <= (ROTATION_THRESHOLD + 10) or
        ROTATION_THRESHOLD <= roll <= (ROTATION_THRESHOLD + 10) or
        ROTATION_THRESHOLD <= yaw <= (ROTATION_THRESHOLD + 10)):
        return True
    return False


while True:
    if detect_rotation():
        print("Sense HAT has been rotated!")
        sense.clear(RED)  # Set LEDs to red
        sense.show_message("Rotated 90!", scroll_speed=0.05, text_colour=[255, 0, 0])
        time.sleep(1)  # Keep red for a second
        sense.clear(GREEN)  # Reset back to green
    
    # Short delay to reduce CPU usage
    time.sleep(0.1)