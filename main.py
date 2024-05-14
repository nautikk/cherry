from flask import Flask

import RPi.GPIO as GPIO

app = Flask(__name__)

# Set the GPIO mode
GPIO.setmode(GPIO.BOARD)

# Define the GPIO pin you want to use
pin_fan = 11  # GPIO pin connected to the fan

# Setup the fan pin as an outpu
GPIO.setup(pin_fan, GPIO.OUT)

@app.route('/turn_on')
def turn_on():
    GPIO.output(pin_fan, GPIO.HIGH)  # Turn on the fan
    return 'Fan turned on'

@app.route('/turn_off')
def turn_off():
    GPIO.output(pin_fan, GPIO.LOW)   # Turn off the fan
    return 'Fan turned off'

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5000)
    finally:
        # Clean up GPIO on exit
        GPIO.cleanup()
