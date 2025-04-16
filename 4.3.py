import RPi.GPIO as GPIO

aux = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(aux, GPIO.OUT)

pwm = GPIO.PWM(aux, 1000)
pwm.start(0)

try:
    while (True):
            duty_cycle = int(input())
            pwm.ChangeDutyCycle(duty_cycle)
            voltage = 3.3 * duty_cycle / 100
            print("voltage = ", voltage)

finally:
    pwm.stop()
    GPIO.output(aux, 0)
    GPIO.cleanup()