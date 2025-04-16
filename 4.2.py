import RPi.GPIO as GPIO
import time

dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

try:
    while (True):
        period = float(input())

        for i in range(1, 256):
            GPIO.output(dac, decimal2binary(i))
            time.sleep(period)

        for i in range(254, -1, -1):
            GPIO.output(dac, decimal2binary(i))
            time.sleep(period)

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
    print("DONE!!!")