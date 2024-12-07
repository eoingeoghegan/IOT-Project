from picamera2 import Picamera2

def capture_image(image_path):
    picam2 = Picamera2()
    picam2.start()
    picam2.capture_file(image_path)
    picam2.stop()
    picam2.close()

if __name__ == "__main__":
    capture_image("/home/egghead1004/images/smart_device.jpg")