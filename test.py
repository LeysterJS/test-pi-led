from gpiozero import LED
import time
import os
import glob
import datetime

# Pin definitions for LEDs
red_led = LED(17)  # Adjust pin numbers based on your setup
green_led = LED(27)
blue_led = LED(22)

# Function to read temperature from DS18B20 sensor
def read_temp_raw():
    base_dir = '/sys/bus/w1/devices/'
    device_folder = glob.glob(base_dir + '28*')[0]
    device_file = device_folder + '/w1_slave'
    with open(device_file, 'r') as f:
        lines = f.readlines()
    return lines

def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos + 2:]
        temp_c = float(temp_string) / 1000.0
        return temp_c

# Setup
def test_led():
    print("Testing LEDs")
    red_led.on()
    time.sleep(1)
    red_led.off()
    green_led.on()
    time.sleep(1)
    green_led.off()
    blue_led.on()
    time.sleep(1)
    blue_led.off()
    print("LED Test complete")

def test_temp_sensor():
    print("Testing Temp Sensor")
    temp_c = read_temp()
    print(f"Current Temperature: {temp_c}°C")
    print("Temp Sensor Test complete")

# Initialize the DS18B20 sensor
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

# Run the tests
test_led()
test_temp_sensor()
