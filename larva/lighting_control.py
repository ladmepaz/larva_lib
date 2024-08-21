import Jetson.GPIO as GPIO
import time


class Light:
    def __init__(self, state=False):
        self.state = state


class LightVariable(Light):
    def __init__(self, pins):
        if not isinstance(pins, list):
            raise ValueError("pins must be a list")
        super().__init__(state=False)
        self.pins = pins  # is a list of pins
        self.pin_on = None
        for pin in self.pins:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, 1)  # 1 is off, 0 is on

    def on(self, pin_on):
        if pin_on not in self.pins:
            raise ValueError("pin not in pins")
        for pin in self.pins:
            if pin != pin_on:
                GPIO.output(pin, 1)  # turn off all other pins
        self.pin_on = pin_on
        GPIO.output(pin_on, 0)  # turn on the selected pin
        self.state = True

    def off(self):
        if self.state:
            GPIO.output(self.pin_on, 1)
            self.pin_on = None
        self.state = False


class LightSimple(Light):
    def __init__(self, pin):
        super().__init__(encendida=False)
        self.pin = pin
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pin, GPIO.OUT)
        GPIO.output(self.pin, 1)  # 1 is off, 0 is on

    def on(self):
        if not self.state:
            GPIO.output(self.pin, 0)
        self.state = True

    def off(self):
        GPIO.output(self.pin, 1)
        self.state = False
