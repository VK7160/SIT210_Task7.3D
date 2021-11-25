import RPi.GPIO as GPIO
import time
from time import sleep

GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

GPIO_TRIGGER =23
GPIO_ECHO = 24
led = 25

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
GPIO.setup(led, GPIO.OUT)

def distance():
    GPIO.output(GPIO_TRIGGER, True)
    
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
    
    StartTime = time.time()
    StopTime = time.time()
    
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
        
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
        
    TimeElapsed = StopTime - StartTime
    
    distance = (TimeElapsed *34000)/2
    
    return distance

p = GPIO.PWM(led, 50)
p.start(0);
if __name__ == '__main__':
    try:
        while True:
            dist = distance()
            print ("Measured Distance = %.lf cm" % dist)
            if distance() <= 10:
                for dc in range (50, 101, 5):
                    p.ChangeDutyCycle(dc)
                    sleep(0.1)
            elif 20 <= distance() > 10:
                for dc in range (11, -1, -5):
                    p.ChangeDutyCycle(dc)
                    sleep(0.1)
                
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        p.stop()
        GPIO.cleanup() 
