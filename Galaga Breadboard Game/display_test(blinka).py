print("hello world")

import displayio #type: ignore
import board #type: ignore
import busio #type: ignore
from adafruit_edp.edp import Adafruit_EPD #type: ignore
from adafruit_epd.ssd1683 import Adafruit_SSD1683 #type: ignore
from adafruit_display_text import label #type: ignore
import terminalio #type: ignore
print("all modules successfully imported, assigning pins and connecting to display")

#set pin connection variables/names
SPI_CLOCK = board.GPIO11() # SPI bus clock signal pin
SPI_MISO = board.GPIO9() # SPI bus input pin
SPI_MOSI = board.GPIO10() # SPI bus output pin
EINK_CHIP_SELECT = board.GPIO8() # eink chip enable pin
EINK_DATACOMMAND = board.GPIO3() # eink data/control pin
SRAM_SELECT = board.GPIO00() #ram chip select pin  FIX THIS <===========
EINK_RST = board.GPIO2() # eink reset pin
EINK_BUSY = board.GPIO14() # eink busy pin

#define constants for display peramiters
DISPLAY_WIDTH = 300
DISPLAY_HIGHT = 400
ROTATION = 0
HILIGHT_COLOR = 0X000000
print("all pins assigned and values ready to be entered")

SPI = busio.SPI(SPI_CLOCK, SPI_MOSI, SPI_MISO) #define clock and data pins for SPI bus (used to talk to display)

DISPLAY_CONNECTION = Adafruit_SSD1683(DISPLAY_HIGHT, DISPLAY_WIDTH, SPI, EINK_CHIP_SELECT, EINK_DATACOMMAND, SRAM_SELECT, EINK_RST, EINK_BUSY) #creat connection for display with its extra pins

WHITE = Adafruit_EPD.WHITE
BLACK = Adafruit_EPD.BLACK
RED = Adafruit_EPD.RED
group = displayio.Group() #create a group to add displayable elements too

text = "hello world"

text_area = label.Label(terminalio.FONT, text=text, color=0xFFFFFF, x=32, y=45, scale=2) #creats formated text

display.root_group = group #display group with elements in it
