from time import sleep
import board
import busio
import adafruit_ssd1327
import displayio
from adafruit_display_text import label
#from displayio import I2CDisplay as I2CDisplayBus
import terminalio
# Release display resources at the start
displayio.release_displays() #required for program to work more than once


print("All modules loaded successfully")
# Set up I2C interface
# SDA = board.SDA
# SCL = board.SCL

i2c = board.STEMMA_I2C()

print("I2C started")
display_bus = displayio.I2CDisplay(i2c, device_address=0x3D)
WIDTH = 128
HEIGHT = 128

display = adafruit_ssd1327.SSD1327(display_bus, width=WIDTH, height=HEIGHT, )

splash = displayio.Group()
display.root_group = splash

def write_to_display(text):
    splash.pop() if len(splash) > 0 else None
    text_area = label.Label(terminalio.FONT, text=text, color=0xFFFFFF, x=32, y=45, scale=2) #creats formated text
    splash.append(text_area) #writes formated text to display
for i in range(5):
    write_to_display('hello\nworld!')
    sleep(2)
    write_to_display('')
    sleep(2)
sleep(10)
displayio.release_displays()
