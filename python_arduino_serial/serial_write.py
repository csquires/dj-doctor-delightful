from time import sleep
import serial

ser = serial.Serial('/dev/ttyACM3',9600)
message = [255,0,0]
for j in range(4):
	for i in message:
		print i
		ser.write(chr(i))
	if j%3 == 0:
		sleep(.1)
sleep(.1)
print "got out of loop"