import RPi.GPIO as GPIO
import time


dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13


GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = 1)
GPIO.setup(comp, GPIO.IN)


def adc():
    value = 128
    GPIO.output(dac, [int(bit) for bit in bin(value)[2:].zfill(8)])
    time.sleep(0.01)
    if (GPIO.input(comp) == 1):
        value -= 64
    else:
        value += 64

    GPIO.output(dac, [int(bit) for bit in bin(value)[2:].zfill(8)])
    time.sleep(0.01)
    if (GPIO.input(comp) == 1):
        value -= 32
    else:
        value += 32

    GPIO.output(dac, [int(bit) for bit in bin(value)[2:].zfill(8)])
    time.sleep(0.01)
    if (GPIO.input(comp) == 1):
        value -= 16
    else:
        value += 16

    GPIO.output(dac, [int(bit) for bit in bin(value)[2:].zfill(8)])
    time.sleep(0.01)
    if (GPIO.input(comp) == 1):
        value -= 8
    else:
        value += 8

    GPIO.output(dac, [int(bit) for bit in bin(value)[2:].zfill(8)])
    time.sleep(0.01)
    if (GPIO.input(comp) == 1):
        value -= 4
    else:
        value += 4

    GPIO.output(dac, [int(bit) for bit in bin(value)[2:].zfill(8)])
    time.sleep(0.01)
    if (GPIO.input(comp) == 1):
        value -= 2
    else:    
        value += 2

    GPIO.output(dac, [int(bit) for bit in bin(value)[2:].zfill(8)])
    time.sleep(0.01)
    if (GPIO.input(comp) == 1):
        value -= 1
    else:
        value += 1
      
    return value

try:
    while True:
            results = adc()
            voltage = 3.3 * results / 256
            print("Voltage = ", voltage)

finally:
    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()
