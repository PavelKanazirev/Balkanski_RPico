import board
import busio
import displayio
# Starting in CircuitPython 9.x fourwire will be a seperate internal library
# rather than a component of the displayio library
try:
    from fourwire import FourWire
except ImportError:
    from displayio import FourWire

from adafruit_st7789 import ST7789

displayio.release_displays()

#spi = board.SPI()
spi = busio.SPI(board.GP18, board.GP19, board.GP16)

while not spi.try_lock():
    pass
spi.configure(baudrate=24000000) # Configure SPI for 24MHz
spi.unlock()
tft_cs = board.GP5
tft_dc = board.GP6

display_bus = FourWire(spi, command=tft_dc, chip_select=tft_cs, reset=board.GP9)

display = ST7789(display_bus, width=320, height=240, rotation=90)

# Make the display context
splash = displayio.Group()
display.root_group = splash

color_bitmap = displayio.Bitmap(320, 240, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0x00FF00

bg_sprite = displayio.TileGrid(color_bitmap,
                               pixel_shader=color_palette,
                               x=0, y=0)
splash.append(bg_sprite)

while True:
    pass