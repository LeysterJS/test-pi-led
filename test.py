from gpiozero import LED
import time

# Pin definitions
red_led = LED(17)  # Adjust pin numbers based on your setup
green_led = LED(27)
blue_led = LED(22)

# Setup
def test_led():
    print("Testing LED")
    red_led.on()
    time.sleep(1)
    red_led.off()
    green_led.on()
    time.sleep(1)
    green_led.off()
    blue_led.on()
    time.sleep(1)
    blue_led.off()
    print("Test complete")

# Run the test
test_led()