from picamera2 import Picamera2

def capture_image(IMAGE_PATH):
    picam2 = Picamera2()
    picam2.start()
    picam2.capture_file(IMAGE_PATH)
    picam2.stop()
    picam2.close()

if __name__ == "__main__":
    capture_image("/home/egghead1004/images/smart_device.jpg")