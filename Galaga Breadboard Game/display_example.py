print("hello world")

import displayio
import board


I2C = board.STEMMA_I2C() #connection to display

DISPLAY = displayio.EPaperDisplay(I2C, address=0x00)