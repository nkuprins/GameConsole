import digitalio

class Button:

    def __init__(self, pin, callback, direction):
        button = digitalio.DigitalInOut(pin)
        button.direction = digitalio.Direction.INPUT
        button.pull = digitalio.Pull.UP
        self._button = button
        self._callback = callback
        self._direction = direction
        self._pressed = False

    def handle(self):
        if not self._button.value and not self._pressed:
            self._pressed = True
            self._callback(self._direction)
        elif self._button.value:
            self._pressed = False

