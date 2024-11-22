import digitalio

# ONLY FOR DEBUGGING
# Class to represent a button
class Button:

    def __init__(self, pin, direction):
        button = digitalio.DigitalInOut(pin)
        button.direction = digitalio.Direction.INPUT
        button.pull = digitalio.Pull.UP
        self._button = button
        self._direction = direction

    def is_pressed(self):
        return not self._button.value

    def get_direction(self):
        return self._direction

