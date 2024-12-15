# SPDX-FileCopyrightText: 2021 John Park for Adafruit Industries
# SPDX-License-Identifier: MIT
# RaspberryPi Pico RP2040 Mechanical Keyboard
# Modified 16/12/2024 for application in a button box for ACC on PS5

import time
import board
from digitalio import DigitalInOut, Direction, Pull
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

print("---Pico Pad Keyboard---")

led = DigitalInOut(board.LED)
led.direction = Direction.OUTPUT
led.value = True

kbd = Keyboard(usb_hid.devices)
cc = ConsumerControl(usb_hid.devices)

# list of pins to use (skipping GP15 on Pico because it's funky)
pins = (
    board.GP0,
    board.GP1,
    board.GP2,
    board.GP3,
    board.GP4,
    board.GP5,
    board.GP6,
    board.GP7,
    board.GP8,
    board.GP9,
    board.GP10,
    board.GP11,
    board.GP12,
    board.GP13,
    board.GP14,
    board.GP16,
    board.GP17,
    board.GP18,
    board.GP19,
    board.GP20,
    board.GP21,
    board.GP22,
    board.GP26,
)

MEDIA = 1
KEY = 2

keymap = {
    (0): (KEY, (Keycode.SHIFT, Keycode.I)),
    (1): (KEY, [Keycode.S]),
    (2): (KEY, (Keycode.ALT, Keycode.L)),
    (3): (KEY, (Keycode.ALT, Keycode.D)),
    (4): (KEY, [Keycode.THREE]),
    (5): (KEY, [Keycode.F2]),
    (6): (KEY, [Keycode.ONE]),
    (7): (KEY, [Keycode.L]),
    (8): (KEY, (Keycode.CTRL, Keycode.L)),
    (9): (KEY, (Keycode.SHIFT, Keycode.L)),
    (10): (KEY, (Keycode.ALT, Keycode.R)),
    (11): (KEY,(Keycode.SHIFT, Keycode.B)),
    (12): (KEY, (Keycode.SHIFT, Keycode.A)),
    (13): (KEY, (Keycode.SHIFT, Keycode.E)),
    (14): (KEY, (Keycode.SHIFT, Keycode.T)),
    (15): (KEY, (Keycode.SHIFT, Keycode.D)),
    (16): (KEY, (Keycode.CTRL, Keycode.D)),
    (17): (KEY, (Keycode.ALT, Keycode.LEFT_ARROW)),
    (18): (KEY, (Keycode.ALT, Keycode.RIGHT_ARROW)),
    (19): (KEY, (Keycode.CTRL, Keycode.B)),
    (20): (KEY, (Keycode.CTRL, Keycode.A)),
    (21): (KEY, (Keycode.CTRL, Keycode.E)),
    (22): (KEY, (Keycode.CTRL, Keycode.T)),
}

switches = []
for i in range(len(pins)):
    switch = DigitalInOut(pins[i])
    switch.direction = Direction.INPUT
    switch.pull = Pull.UP
    switches.append(switch)


switch_state = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

while True:
    for button in range(24):
        if switch_state[button] == 0:
            if not switches[button].value:
                try:
                    if keymap[button][0] == KEY:
                        kbd.press(*keymap[button][1])
                    else:
                        cc.send(keymap[button][1])
                except ValueError:  # deals w six key limit
                    pass
                switch_state[button] = 1

        if switch_state[button] == 1:
            if switches[button].value:
                try:
                    if keymap[button][0] == KEY:
                        kbd.release(*keymap[button][1])

                except ValueError:
                    pass
                switch_state[button] = 0

    time.sleep(0.01)  # debounce
