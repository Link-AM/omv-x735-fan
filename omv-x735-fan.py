#!/usr/bin/env python3

import RPi.GPIO as GPIO
import subprocess
import time

from gpiozero import OutputDevice

SLEEP_INTERVAL = 3  # (seconds) How often we check the core temperature.
GPIO_PIN = 13  # Which GPIO pin you're using to control the fan.
DEBUG_LOGGING = False

def setup():
    if DEBUG_LOGGING: print('Setting up GPIO...')
    global pwm
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(GPIO_PIN, GPIO.OUT)
    GPIO.output(GPIO_PIN, GPIO.LOW)
    pwm = GPIO.PWM(GPIO_PIN, 25000)
    pwm.start(0)
    if DEBUG_LOGGING: print('GPIO setup complete.')

def get_temp():
    output = subprocess.run(['vcgencmd', 'measure_temp'], capture_output=True)
    temp_str = output.stdout.decode()
    try:
        return float(temp_str.split('=')[1].split('\'')[0])
    except (IndexError, ValueError):
        raise RuntimeError('Could not parse temperature output.')

def loop():
    while True:
        temp = get_temp()
        if DEBUG_LOGGING: print('Core temperature:', temp)

        if temp > 70:
            if DEBUG_LOGGING: print('temp > 70, setting fan to 100%')
            pwm.ChangeDutyCycle(100)
        elif temp > 60:
            if DEBUG_LOGGING: print('temp > 60, setting fan to 75%')
            pwm.ChangeDutyCycle(80)
        elif temp > 50:
            if DEBUG_LOGGING: print('temp > 50, setting fan to 50%')
            pwm.ChangeDutyCycle(60)
        elif temp > 40:
            if DEBUG_LOGGING: print('temp > 40, setting fan to 25%')
            pwm.ChangeDutyCycle(40)
        elif temp > 30:
            if DEBUG_LOGGING: print('temp > 30, setting fan to 10%')
            pwm.ChangeDutyCycle(20)
        else:
            if DEBUG_LOGGING: print('temp < 30, setting fan to 0%')
            pwm.ChangeDutyCycle(0)

        time.sleep(SLEEP_INTERVAL)

def destroy():
    if DEBUG_LOGGING: print('Cleaning up GPIO...')
    pwm.stop()
    GPIO.output(GPIO_PIN, GPIO.LOW)
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()