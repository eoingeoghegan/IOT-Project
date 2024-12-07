import BlynkLib
from time import sleep

#Blynk authentication token and Created an instance of Blynk
BLYNK_AUTH_TOKEN = "6JwZ0zMXTepx2ElsQJrPAjot77d8iu7a"
blynk = BlynkLib.Blynk(BLYNK_AUTH_TOKEN)

@blynk.on("V0")
def button_v1_write(value):
    button_value = value[0]
    print(f'Current button value: {button_value}')

if __name__ == "__main__":
    print("Blynk application started. Listening for events...")
    try:
        while True:
            blynk.run()  # Process Blynk events
            sleep(2)  # Add a short delay to avoid high CPU usage
    except KeyboardInterrupt:
        print("Blynk application stopped.")
    try:
        blynk.run()
    except KeyboardInterrupt:
        print("Blynk has stopped")
    sleep(2)