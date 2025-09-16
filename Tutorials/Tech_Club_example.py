import board #type: ignore
import busio #type: ignore
import digitalio #type: ignore
from time import sleep

# set up I2C bus for communication with devices.
I2C = board.STEMMA_I2C()


import displayio, adafruit_ssd1327, terminalio #type: ignore
displayio.release_displays() #clear and release displays from previos aplication
from adafruit_display_text import label #type: ignore
display_bus = displayio.I2CDisplay(I2C, device_address=0x3D)
WIDTH = 128
HEIGHT = 128
display = adafruit_ssd1327.SSD1327(display_bus, width=WIDTH, height=HEIGHT)
splash = displayio.Group() #create display environment
display.root_group = splash #attach display environment to display
FONTSCALE = 1
BORDER = 8
def clear_unlock_display():
    displayio.release_displays()

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
encoder_pos = label.Label(terminalio.FONT, text="0", color=0xFFFFFF, x=8, y=12, scale=2)
encoder_button = label.Label(terminalio.FONT, text="Button: Not Pressed", color=0xFFFFFF, x=5, y=30, scale=1)



from adafruit_seesaw import seesaw, rotaryio, digitalio #type: ignore
seesaw = seesaw.Seesaw(I2C, addr=0x36)
seesaw.pin_mode(24, seesaw.INPUT_PULLUP)  # Configure seesaw pin used to read knob button presses
button = digitalio.DigitalIO(seesaw, 24)  # The internal pull up is enabled to prevent floating input
ENButton_held = False #encoder button hold variable
encoder = rotaryio.IncrementalEncoder(seesaw)

# Add encoder position label to display
splash.append(encoder_pos)
# Add button state label to display
splash.append(encoder_button)


def write_encoder_pos_display(encoder_value): # Update encoder position text
    encoder_pos.text = encoder_value  

def write_encoder_button_display(button_pressed):    # Update button state text
    encoder_button.text = f"Button: {button_pressed}"
last_position = None

while True:
    
    position = -encoder.position # negate the position to make clockwise rotation positive

    if position != last_position: #if the position of the encoder dose not match last known, update last known and writes position to display
        last_position = position
        print("Position: {}".format(position))
        write_encoder_pos_display("{}".format(position))

    if not button.value and not ENButton_held: # checks if button is pressed or if it is being continualy pressd
        ENButton_held = True
        print("Button pressed")
        write_encoder_button_display("Pressed")

    if button.value and ENButton_held: # returns false when button is no longer being pressed
        ENButton_held = False
        print("Button released")
        write_encoder_button_display("Not Pressed")






