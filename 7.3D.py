import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(19, GPIO.IN)
GPIO.setup(26, GPIO.OUT)

trig = 13
echo = 19
led = 26

pwm = GPIO.PWM(21, 100)                 
pwm.start(100)

def cal_distance():
    GPIO.output(trig, True)
    
    time.sleep(0.00001)
    GPIO.output(trig, False)

    start = time.time()
    stop  = time.time()

    while GPIO.input(echo) == 0:
        start = time.time()
    
    while GPIO.input(echo) == 1:
        stop = time.time()

    elapse_time = stop - start
    distance = (elapse_time * 34300) / 2
    return distance

try: 
  while True:
       dist = cal_distance()
       if(dist > 40):
          pwm.ChangeDutyCycle(30)
          time.sleep(2)
       elif(dist > 25 and dist <40):
          pwm.ChangeDutyCycle(60)
          time.sleep(2)
       elif(dist > 15 and dist <25):
          pwm.ChangeDutyCycle(100) 
          time.sleep(2)
       else:
          pwm.ChangeDutyCycle(20)
          time.sleep(2)
          
except KeyboardInterrupt:
        print("Measurement stopped by User")
        p.stop()
        GPIO.cleanup() 