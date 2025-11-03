#import dependencies for pin control
import board #type: ignore
import busio #type: ignore
import digitalio #type: ignore
#import EInk display drivers
from adafruit_epd.epd import Adafruit_EPD #type: ignore
from adafruit_epd.ssd1683 import Adafruit_SSD1683 #type: ignore
print("all modules successfully imported, assigning pins and connecting to display")

#set pin connection variables/names
SPI_CLOCK = board.SCK # SPI bus clock signal pin
SPI_MISO = board.MISO # SPI bus input pin
SPI_MOSI = board.MOSI # SPI bus output pin
EINK_CHIP_SELECT = digitalio.DigitalInOut(board.D0) # eink chip enable pin
EINK_DATACOMMAND = digitalio.DigitalInOut(board.D22) # eink data/control pin
SRAM_SELECT = None #board.GPIO00() #ram chip select pin  FIX THIS <===========
EINK_RST =digitalio.DigitalInOut(board.D27) # eink reset pin
EINK_BUSY = digitalio.DigitalInOut(board.D17) # eink busy pin

#define constants for display peramiters
DISPLAY_WIDTH = 300
DISPLAY_HIGHT = 400
ROTATION = 0
print("all pins assigned and values ready to be entered")
#define clock and data pins for SPI bus (used to talk to display)
SPI = busio.SPI(SPI_CLOCK, SPI_MOSI, SPI_MISO) 
print("SPI bus created, connecting to display")

#create connection for display with its extra pins
display = Adafruit_SSD1683(DISPLAY_HIGHT, DISPLAY_WIDTH, SPI, cs_pin=EINK_CHIP_SELECT, dc_pin=EINK_DATACOMMAND, sramcs_pin=SRAM_SELECT, rst_pin=EINK_RST, busy_pin=EINK_BUSY) 

#define display colors and rotation
display.rotation = ROTATION
WHITE = Adafruit_EPD.WHITE
BLACK = Adafruit_EPD.BLACK
RED = Adafruit_EPD.RED

text = "hello cruel worl"
x=50
y=25
import time as T
print("blanking display")
display.fill(WHITE)
T.sleep(3)
display.display()

T.sleep(8)
print("displaying text")
display.text(text, x, y, color=RED, font_name='font5x8.bin')
display.display()

