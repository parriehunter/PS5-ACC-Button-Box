# PS5-ACC-Button-Box

Creating a Button Box to be used on a PS5 for Assetto Corsa Competizione.

This will use a Raspberry Pi Pico 2 with switches and buttons from Aliexpress.

Configuring the Pico to use the ACC Keyboard Shortcuts that are described here https://solox.gg/acc-keyboard-shortcuts/

Code based on https://learn.adafruit.com/diy-pico-mechanical-keyboard-with-fritzing-circuitpython

## Parts List

<ul>
  <li>12mm Push Buttons - https://vi.aliexpress.com/item/1005004556149934.html</li>
  <li>Junction Box - 200x120x56mm - https://vi.aliexpress.com/item/1005005367221276.html</li>
  <li>3 Position Rotary Switch - https://vi.aliexpress.com/item/1005007167641825.html</li>
  <li>19mm Flat push Button Switch - https://vi.aliexpress.com/item/1005004765834557.html</li>
  <li>16mm Push Buttons - https://vi.aliexpress.com/item/1005005906389808.html</li>
  <li>Toggle Switch with Cover - https://vi.aliexpress.com/item/1005004068738380.html</li>
  <li>Momentary Toggle Switch - https://vi.aliexpress.com/item/1005004367116021.html</li>
  <li>Jumper Cable - https://vi.aliexpress.com/item/4000943168064.html</li>
  <li>Mounting Bracket - https://vi.aliexpress.com/item/1005007642026372.html</li>
</ul>

## Install the prerequisites and the code

Use this guide https://learn.adafruit.com/diy-pico-mechanical-keyboard-with-fritzing-circuitpython to be able to load the requirements and the code. 

Quick Guide
<ol>
  <li>Install CircuitPython onto the Pico</li>
      <ol>
        <li>Download the correct .UF2 circuitpython file. These are located either at https://circuitpython.org/board/raspberry_pi_pico/ or https://circuitpython.org/board/raspberry_pi_pico2/ depending on the version of Pico you have</li>
        <li>Copy the .UF2 file onto the mounted drive</li>
        <li>The Pico will automatically reboot and install circuit python</li></li>
      </ol>
  <li>Install the Adafruit HID Library
    <ol>
      <li>Copy the lib folder to the root directory of the Pico</li>
    </ol>
  </li>
  <li>Copy code.py to the root directory of the Pico</li>
  <li>The Pico is ready</li>
</ol>

## Mounting Switches

Here is the picture of the button layout.
[![The Switch Layout](/assets/img/Button.Box.Switch.Drawing.png)](https://github.com/parriehunter/PS5-ACC-Button-Box/blob/595b8a9aa02864b91d77672111bb2e55841cd3c6/assets/img/Button.Box.Drawing.png)


## Wire up the Switches to the Pico

How I am planning to wire all the switches to the Pico
[![Wiring Diagram](/assets/img/Button.Box.Wiring.Drawing.png)](https://github.com/parriehunter/PS5-ACC-Button-Box/blob/c64d351191bc0df918ce5761ca17e5b0fad25a2d/assets/img/Button.Box.Wiring.Drawing.png)

## Mount the Button Box to the Sim Rig
Tsing this bracket. https://vi.aliexpress.com/item/1005007642026372.html
