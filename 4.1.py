import RPi.GPIO as GPIO

dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

try:
    while True:
        value = input()
        try:
            value = int(value)
            if value < 0 or value > 255:
                print("Value must be in range [0, 256)")
                continue

            GPIO.output(dac, decimal2binary(value))
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
    GPIO.cleanup()
    print("DONE!!!")
