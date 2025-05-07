import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt

dac = [8, 11, 7, 1, 0, 5, 12, 6]  
comp = 14  
troyka = 13
leds = [9, 10, 22, 27, 17, 4, 3, 2]  

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=0)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(leds, GPIO.OUT)

def decimal_to_binary_list(n):
    return [int(bit) for bit in bin(n)[2:].zfill(8)]

def adc():
    value = 128
    GPIO.output(dac, [int(bit) for bit in bin(value)[2:].zfill(8)])
    time.sleep(0.0022)
    if (GPIO.input(comp) == 1):
        value -= 128

    value += 64
    GPIO.output(dac, [int(bit) for bit in bin(value)[2:].zfill(8)])
    time.sleep(0.0022)
    if (GPIO.input(comp) == 1):
        value -= 64

    value += 32
    GPIO.output(dac, [int(bit) for bit in bin(value)[2:].zfill(8)])
    time.sleep(0.0022)
    if (GPIO.input(comp) == 1):
        value -= 32

    value += 16
    GPIO.output(dac, [int(bit) for bit in bin(value)[2:].zfill(8)])
    time.sleep(0.0022)
    if (GPIO.input(comp) == 1):
        value -= 16

    value += 8
    GPIO.output(dac, [int(bit) for bit in bin(value)[2:].zfill(8)])
    time.sleep(0.0022)
    if (GPIO.input(comp) == 1):
        value -= 8

    value += 4
    GPIO.output(dac, [int(bit) for bit in bin(value)[2:].zfill(8)])
    time.sleep(0.0022)
    if (GPIO.input(comp) == 1):
        value -= 4
    
    value += 2
    GPIO.output(dac, [int(bit) for bit in bin(value)[2:].zfill(8)])
    time.sleep(0.0022)
    if (GPIO.input(comp) == 1):
        value -= 2

    value += 1
    GPIO.output(dac, [int(bit) for bit in bin(value)[2:].zfill(8)])
    time.sleep(0.0022)
    if (GPIO.input(comp) == 1):
        value -= 1

    return value

def light_leds(value):
    num_led = int(value / 256.0 * 8)
    for i in range(8):
        GPIO.output(leds[i], 1 if i < num_led else 0)

try:
    measurements = []  
    start_time = time.time()  

    GPIO.output(troyka, 1)  
    while True:
        voltage = adc() * 3.3 / 256.0
        measurements.append(voltage)
        if voltage >= 2.66:  
            break
        # time.sleep(0.0022)

    GPIO.output(troyka, 0)  
    while True:
        voltage = adc() * 3.3 / 256.0
        if voltage <= 3.3 * 0.02:  
            break
        measurements.append(voltage)
        # time.sleep(0.0022)

    end_time = time.time()  
    duration = end_time - start_time  

    with open("data.txt", "w") as file:
        for value in measurements:
            file.write(f"{value}\n")

    sampling_rate = len(measurements) / duration
    quantization_step = 3.3 / 256.0

    with open("settings.txt", "w") as file:
        file.write(f"Average sampling rate: {sampling_rate:.2f} Гц\n")
        file.write(f"ADC quantization step: {quantization_step:.4f} В\n")

    plt.plot(measurements)
    plt.title("Voltage versus time")
    plt.xlabel("Measurement number")
    plt.ylabel("Voltage, V")
    plt.show()

    print(f"Total duration of the experiment: {duration:.2f} s")
    print(f"Period of one measurement: {duration / len(measurements):.4f} s")
    print(f"Average sampling rate: {sampling_rate:.2f} Hz")
    print(f"ADC quantization step: {quantization_step:.4f} V")

finally:
    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    GPIO.output(leds, 0)
    GPIO.cleanup()
