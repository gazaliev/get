import RPi.GPIO as GPIO
import time


dac = [8, 11, 7, 1, 0, 5, 12, 6]
led = [2, 3, 4, 17, 27, 22, 10, 9]
comp = 14
troyka = 13


GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = 1)
GPIO.setup(comp, GPIO.IN)


def adc():
    value = 128
    GPIO.output(dac, [int(bit) for bit in bin(value)[2:].zfill(8)])
    time.sleep(0.005)
    if (GPIO.input(comp) == 1):
        value -= 128

    value += 64
    GPIO.output(dac, [int(bit) for bit in bin(value)[2:].zfill(8)])
    time.sleep(0.005)
    if (GPIO.input(comp) == 1):
        value -= 64

    value += 32
    GPIO.output(dac, [int(bit) for bit in bin(value)[2:].zfill(8)])
    time.sleep(0.005)
    if (GPIO.input(comp) == 1):
        value -= 32

    value += 16
    GPIO.output(dac, [int(bit) for bit in bin(value)[2:].zfill(8)])
    time.sleep(0.005)
    if (GPIO.input(comp) == 1):
        value -= 16

    value += 8
    GPIO.output(dac, [int(bit) for bit in bin(value)[2:].zfill(8)])
    time.sleep(0.005)
    if (GPIO.input(comp) == 1):
        value -= 8

    value += 4
    GPIO.output(dac, [int(bit) for bit in bin(value)[2:].zfill(8)])
    time.sleep(0.005)
    if (GPIO.input(comp) == 1):
        value -= 4
    
    value += 2
    GPIO.output(dac, [int(bit) for bit in bin(value)[2:].zfill(8)])
    time.sleep(0.005)
    if (GPIO.input(comp) == 1):
        value -= 2

    value += 1
    GPIO.output(dac, [int(bit) for bit in bin(value)[2:].zfill(8)])
    time.sleep(0.005)
    if (GPIO.input(comp) == 1):
        value -= 1
    
      
    return value

try:
    while True:
            try:
                value = adc()
                if value < 0 or value > 255:
                    print("Value must be in range [0, 256)")
                    continue
                
                list = [int(bit) for bit in bin(value)[2:].zfill(8)]

                for i in range(8):
                    if list[i] == 1:
                        for j in range(i, 8):
                            list[j] = 1
                        break
                
                GPIO.output(led, list)
                voltage = 3.3 * value / 256
                print ('Voltage = ', voltage)

            except ValueError or TypeError:
                try:
                    value = float(value)
                    print("Type cannot be float")
                except:
                    if value == 'q':
                        break
                    print("Incorrect value") 

finally:
    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()
