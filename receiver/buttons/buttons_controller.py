import board
import asyncio
from properties.direction import Direction
from buttons.button import Button

# ONLY FOR DEBUGGING
# Listens for button presses and calls callback function on them
async def run(buttons, callback):
    while True:
        for button in buttons:
            if button.is_pressed():
                callback(button.get_direction())
                break
        await asyncio.sleep(0.0)

# ONLY FOR DEBUGGING
def create_buttons():
    left_btn = Button(board.GP18, Direction.LEFT)
    right_btn = Button(board.GP22, Direction.RIGHT)
    up_btn = Button(board.GP27, Direction.UP)
    down_btn = Button(board.GP28, Direction.DOWN)
    return [left_btn, right_btn, up_btn, down_btn]
