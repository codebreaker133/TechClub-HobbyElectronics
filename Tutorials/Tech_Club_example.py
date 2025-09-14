import board #type: ignore
import busio #type: ignore
import digitalio #type: ignore

# set up I2C bus for communication with devices.
I2C = board.STEMMA_I2C()


import displayio, adafruit_ssd1327, terminalio #type: ignore
displayio.release_displays() #clear and release displays from previos aplication
from adafruit_display_text import label #type: ignore
displaybus = displayio.I2CDisplay(I2C, device_address=0x3D)
display = adafruit_ssd1327.SSD1327(displaybus, width=128, height=128)
splash = displayio.Group() #create display environment
display.root_group = splash #attach display environment to display
FONTSCALE = 1
BORDER = 8

# Draw a label
text = "Hello World!"
text_area = label.Label(terminalio.FONT, text=text, color=0xFFFFFF)
text_width = text_area.bounding_box[2] * FONTSCALE
text_group = displayio.Group(
    scale=FONTSCALE,
    x=display.width // 2 - text_width // 2,
    y=display.height // 2,
)
text_group.append(text_area)  # Subgroup for text scaling
splash.pop() if len(splash) > 0 else None
splash.append(text_group)




boardButton = digitalio.DigitalInOut(board.BUTTON) #set up BOOT button as digital input (on board button NOT on encoder)
boardButton.switch_to_input(pull=digitalio.Pull.UP) #set pins for proper input control 


from adafruit_seesaw import digitalio, rotaryio, seesaw #type: ignore
seesaw = seesaw.Seesaw(I2C, 0x36) #defining encoder addr and starting seesaw driver for encoder
seesaw.pin_mode(24, seesaw.INPUT_PULLUP) #set pins for proper input control 
button = digitalio.DigitalIO(seesaw, 24) #defineing encoder button
ENButton_held = False #encoder button hold variable








