import serial #import Serial

print ("all good")

ser = serial.Serial()
ser.baudrate = 9600
ser.port = "COM9"
#ser.parity = serial.PARITY_EVEN
ser.rtscts = 1

ser.close()
ser.open()

while (1 == 1):

    if (ser.inWaiting() > 0):
        myData = ser.readline()
        print(myData.decode('utf-8'))









