import Jetson.GPIO as GPIO
import time


class StepperMotor:
    def __init__(self, M_pins, FC_pin, sequence=4, delay=0.001):
        if sequence not in [4, 8]:
            raise ValueError('Sequence must be 4 or 8')

        self.m_pins = M_pins
        self.fc_pin = FC_pin
        self.delay = delay
        self.counter = 0

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.fc_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        for pin in self.m_pins:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, 0)

        if sequence == 4:
            self.sequence = [[1, 0, 0, 0],
                             [0, 1, 0, 0],
                             [0, 0, 1, 0],
                             [0, 0, 0, 1]]

        else:
            self.sequence = [[1, 0, 0, 0],
                             [1, 1, 0, 0],
                             [0, 1, 0, 0],
                             [0, 1, 1, 0],
                             [0, 0, 1, 0],
                             [0, 0, 1, 1],
                             [0, 0, 0, 1],
                             [1, 0, 0, 1]]

        self.step_count = len(self.sequence)

    def step(self, steps, direction=1):
        if direction not in [-1, 1]:
            raise ValueError('Direction must be 1 or -1')
        elif direction == 1:
            seq = self.sequence
        else:
            seq = self.sequence[::-1]

        for _ in range(steps):
            for i in range(self.step_count):
                for pin in range(4):
                    GPIO.output(self.m_pins[pin], seq[i][pin])
            self.counter += direction
            time.sleep(self.delay)

    def origen(self):
        if GPIO.input(self.fc_pin) != 0:  # change if using pull-up or pull-down
            self.step(1, -1)
        else:
            self.counter = 0

    def cleanup(self):
        GPIO.cleanup()
