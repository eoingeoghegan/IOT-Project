from sense_hat import SenseHat

# This is the message to send to a server
# {"deviceID": "Device1", "temp": 36.32, "humidity": 37.44}

# create a function to retrieve the temp + humidity

def smart_device_data(deviceID):
    sense =SenseHat() #can access the temp and humid now
    temp = sense.get_temperature()
    adjusted_temp = temp - 14.5 #stored as temp
    humidity = sense.get_humidity()

    #turn it into json format
        # in the function param(deviceID) this will be a name entered by the user of a device
        #device_data has will use the entered ID to the format below and show the temp and humid
        #this is template for a device
    device_data = {
        "deviceID": deviceID,
        "temp": round(adjusted_temp, 2),
        "humidity": round(humidity, 2)
    }
    
    return device_data


if __name__ == "__main__":
    #will enter a name for deviceID for test
    deviceID = "Smart Care Device"
    device_data = smart_device_data(deviceID)

    print (device_data)