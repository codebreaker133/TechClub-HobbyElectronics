print("hello world")

import displayio #type: ignore
import board #type: ignore
import FourWire #type: ignore
import adafruit_ssd1683 #type: ignore
from adafruit_display_text import label #type: ignore
import terminalio #type: ignore
print("all modules successfully imported, assigning pins and connecting to display")

#set pin connection variables/names
SPI_CLOCK = board.GPIO11() # SPI bus clock signal pin
SPI_MOSI = board.GPIO10() # SPI bus output pin
EINK_ENABLE = board.GPIO8() # eink chip enable pin
EINK_DATACOMMAND = board.GPIO3() # eink data/control pin
EINK_RST = board.GPIO2() # eink reset pin
EINK_BUSY = board.GPIO14() # eink busy pin

#define constants for display peramiters
DISPLAY_WIDTH = 300
DISPLAY_HIGHT = 400
ROTATION = 0
HILIGHT_COLOR = 0X000000
print("all pins assigned and values ready to be entered")

SPI = board.SPI() #define clock and data pins for SPI bus (used to talk to display)

DISPLAY_CONNECTION = FourWire(SPI,  EINK_DATACOMMAND, EINK_ENABLE, EINK_RST, baudrate=1000000) #creat connection for display with its extra pins

display = adafruit_ssd1683(DISPLAY_CONNECTION, DISPLAY_WIDTH, DISPLAY_HIGHT, ROTATION, EINK_BUSY, HILIGHT_COLOR) #assign that bus to the display driver

group = displayio.Group() #create a group to add displayable elements too

text = "hello world"

text_area = label.Label(terminalio.FONT, text=text, color=0xFFFFFF, x=32, y=45, scale=2) #creats formated text

display.root_group = group #display group with elements in it