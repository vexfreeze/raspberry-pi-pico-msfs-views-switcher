import time
import board
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

print("---Start---")
kbd = Keyboard(usb_hid.devices)

def Send(*keycodes: int) -> None:
    kbd.press(*keycodes)
    time.sleep(0.100)
    kbd.release(*keycodes)

def SendAndWait(*keycodes: int) -> None:
    kbd.press(*keycodes)
    time.sleep(0.100)
    kbd.release(*keycodes)
    time.sleep(5.000)

time.sleep(5.000)

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
    if i >= actions_count:
        i = 0
    
    action = actions[i]
    if action[0] == SEND:
        Send(*action[1])
    
    if action[0] == SENDANDWAIT:
        SendAndWait(*action[1])
    
    i = i + 1      

print("---Done---")
