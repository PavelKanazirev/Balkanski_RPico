# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT
# https://docs.circuitpython.org/projects/st7789/en/latest/examples.html
"""
This test will initialize the display using displayio and draw a solid green
background, a smaller purple rectangle, and some yellow text.
"""
import board
import busio
import terminalio
import displayio
import digitalio
import time

# Starting in CircuitPython 9.x fourwire will be a seperate internal library
# rather than a component of the displayio library
try:
    from fourwire import FourWire
except ImportError:
    from displayio import FourWire
from adafruit_display_text import label
from adafruit_st7789 import ST7789

# Release any resources currently in use for the displays
displayio.release_displays()

#spi = board.SPI()
spi = busio.SPI(board.GP18, board.GP19, board.GP16)
tft_cs = board.GP5
tft_dc = board.GP6

display_bus = FourWire(spi, command=tft_dc, chip_select=tft_cs, reset=board.GP9)

display = ST7789(display_bus, width=320, height=240, rotation=90)

# Make the display context
splash = displayio.Group()
display.root_group = splash

color_bitmap = displayio.Bitmap(320, 240, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0x00FF77  # Bright Green

bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=20, y=10)
splash.append(bg_sprite)

# Draw a label
text_group = displayio.Group(scale=6, x=69, y=69)
text = "{}".format("Safe")
text_area = label.Label(terminalio.FONT, text=text, color=(0x000000))
text_group.append(text_area)	# Subgroup for text scaling
splash.append(text_group)

inputPin = digitalio.DigitalInOut(board.GP21)
inputPin.pull = digitalio.Pull.UP
outputPin = digitalio.DigitalInOut(board.GP22)
outputPin.direction = digitalio.Direction.OUTPUT

while True:
    if inputPin.value != 0 :
        outputPin.value = False
        text = str("{}".format("SAFE!"))
        text_area.text = text
        color_palette[0] = 0x00FF77  # Green
        bg_sprite.pixel_shader=color_palette
    else :
        outputPin.value = True
        text = str("{}".format("ALERT!"))
        text_area.text = text
        color_palette[0] = 0xFF0000  # Red
        bg_sprite.pixel_shader=color_palette

    time.sleep(0.2)