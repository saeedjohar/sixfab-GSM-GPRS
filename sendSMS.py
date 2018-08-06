# This script sends SMS from Sixfab GSM/SPRS shield
# for running it: python sendSMS.py <serial0/USB0> <NUMBER> <"Your Message">


import sys
import serial
from time import sleep

NUM = sys.argv[2]
MSG = sys.argv[3]

SERIAL_PORT = '/dev/' + sys.argv[1]
SERIAL_RATE = 115200
ser = serial.Serial(SERIAL_PORT,SERIAL_RATE)


OPERATE_SMS_MODE = 'AT+CMGF=1\r'
SEND_SMS = 'AT+CMGS="%s"\r' %NUM

ser.write('\x1A') #sending CTRL-Z
#https://en.wikipedia.org/wiki/ASCII


def main():
	print "Sending SMS to %s" %NUM
	if not ser.is_open:
		ser.open()

	if ser.is_open:
		ser.write(OPERATE_SMS_MODE)
		sleep(0.5)
		ser.write(SEND_SMS)
		sleep(0.1)
		ser.write(MSG)
		sleep(0.1)
		ser.write('\x1A')	#sending CTRL-Z
							#https://en.wikipedia.org/wiki/ASCII
		sleep(0.5)





if __name__ == "__main__":
	try:
		main()
	except Exception as e:
		print 'Error: ' + str(e)