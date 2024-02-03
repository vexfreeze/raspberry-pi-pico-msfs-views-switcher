import time
import board
import digitalio

import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

btn = digitalio.DigitalInOut(board.GP7)
btn.direction = digitalio.Direction.INPUT
btn.pull = digitalio.Pull.UP
led = digitalio.DigitalInOut(board.GP16)
led.direction = digitalio.Direction.OUTPUT
button_state = 0
led_state = 0

kbd = Keyboard(usb_hid.devices)

def wait_button(seconds: float) -> None:
    for x in range(10):
        global button_state
        global led_state
        last_state = button_state
        button_state = btn.value
        if not button_state and last_state:
            led_state = not(led_state)
            led.value = led_state
        time.sleep(0.1) # sleep for debounce

def send(*keycodes: int) -> None:
    kbd.press(*keycodes)
    wait_button(0.1)
    kbd.release(*keycodes)

def send_and_wait(*keycodes: int) -> None:
    kbd.press(*keycodes)
    wait_button(0.1)
    kbd.release(*keycodes)
    wait_button(5.0)

SEND = 0
SENDANDWAIT = 1

actions_count = 25
actions = [
    (SEND, [Keycode.END]),
    (SEND, (Keycode.SHIFT, Keycode.SPACE)),
    (SENDANDWAIT, (Keycode.SHIFT, Keycode.D)),
    (SENDANDWAIT, (Keycode.SHIFT, Keycode.D)),
    (SENDANDWAIT, (Keycode.SHIFT, Keycode.D)),
    (SENDANDWAIT, (Keycode.SHIFT, Keycode.D)),
    (SENDANDWAIT, (Keycode.SHIFT, Keycode.D)),
    (SENDANDWAIT, (Keycode.SHIFT, Keycode.D)),
    (SENDANDWAIT, (Keycode.SHIFT, Keycode.D)),
    (SENDANDWAIT, (Keycode.SHIFT, Keycode.D)),
    (SENDANDWAIT, (Keycode.SHIFT, Keycode.D)),
    (SEND, (Keycode.SHIFT, Keycode.SPACE)),
    (SEND, [Keycode.END]),
    (SEND, (Keycode.SHIFT, Keycode.SPACE)),
    (SENDANDWAIT, (Keycode.SHIFT, Keycode.ONE)),
    (SENDANDWAIT, (Keycode.SHIFT, Keycode.TWO)),
    (SENDANDWAIT, (Keycode.SHIFT, Keycode.THREE)),
    (SENDANDWAIT, (Keycode.SHIFT, Keycode.FOUR)),
    (SENDANDWAIT, (Keycode.SHIFT, Keycode.FIVE)),
    (SENDANDWAIT, (Keycode.SHIFT, Keycode.SIX)),
    (SENDANDWAIT, (Keycode.SHIFT, Keycode.SEVEN)),
    (SENDANDWAIT, (Keycode.SHIFT, Keycode.EIGHT)),
    (SENDANDWAIT, (Keycode.SHIFT, Keycode.NINE)),
    (SENDANDWAIT, (Keycode.SHIFT, Keycode.ZERO)),
    (SENDANDWAIT, (Keycode.SHIFT, Keycode.SPACE))
]

i = 0
while True:
    if not led_state:
        i = 0
        wait_button(0.1)
        continue;
    
    if i >= actions_count:
        i = 0
    
    action = actions[i]
    if action[0] == SEND:
        send(*action[1])
    
    if action[0] == SENDANDWAIT:
        send_and_wait(*action[1])
    
    i = i + 1
