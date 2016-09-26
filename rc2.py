# import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
# GPIO.setmode(GPIO.BOARD)
GPIO.setup(27,GPIO.OUT)   #Left motor input A 13
GPIO.setup(22,GPIO.OUT)   #Left motor input B 15
GPIO.setup(24,GPIO.OUT)  #Right motor input A 18
GPIO.setup(25,GPIO.OUT)  #Right motor input B 22
GPIO.setwarnings(False)

while True:
    print "Rotating both motors in clockwise direction"
    GPIO.output(27,1)
    GPIO.output(22,0)
    GPIO.output(24,1)
    GPIO.output(25,0)
    time.sleep(1)     #One second delay

    print "Rotating both motors in anticlockwise direction"
    GPIO.output(27, 0)
    GPIO.output(22,1)
    GPIO.output(24,0)
    GPIO.output(25,1)
    time.sleep(1)     