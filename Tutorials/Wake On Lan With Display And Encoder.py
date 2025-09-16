import board
import busio
from time import sleep
import os, wifi, socketpool # for wifi and WOL
from adafruit_seesaw import seesaw, rotaryio, digitalio
import adafruit_displayio_ssd1306, displayio # for display output
from adafruit_display_text import label # for display text formating
import terminalio # for display font
def clear_unlock_display():
    displayio.release_displays()
clear_unlock_display()
SDA = board.GP0
SCL = board.GP1
i2c = busio.I2C(SCL, SDA)

DESKTOP_MAC_ADDR = b"\x40\xec\x99\x9a\xfd\xe4"

# Display init
display_bus = displayio.I2CDisplay(i2c, device_address=0x3D)
WIDTH = 128
HEIGHT = 64
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=WIDTH, height=HEIGHT)
splash = displayio.Group()
display.root_group = splash

# Create the label for encoder position, button state, and computer select 
encoder_pos = label.Label(terminalio.FONT, text="0", color=0xFFFFFF, x=8, y=12, scale=2)
encoder_button = label.Label(terminalio.FONT, text="Button: Not Pressed", color=0xFFFFFF, x=5, y=30, scale=1)
slct = label.Label(terminalio.FONT, text="no stored value", color=0xFFFFFF, x=5, y=40) # computer selector display

# Add encoder position label to display
splash.append(encoder_pos)
# Add button state label to display
splash.append(encoder_button)
# Add selector to display
splash.append(slct)

def WoL_Desktop(address_in): # wakes selected mac address via WOL
    print("Connecting to Wi-Fi...")
    wifi.radio.connect(os.getenv('CIRCUITPY_WIFI_SSID'), os.getenv('CIRCUITPY_WIFI_PASSWORD'))
    print("Connected to Wi-Fi!")
    pool = socketpool.SocketPool(wifi.radio)
    # Create UDP socket for Magic Packet
    sock = pool.socket(pool.AF_INET, pool.SOCK_DGRAM)

    # Target MAC address (replace this with the actual MAC address of the computer you want to wake)
    target_mac = address_in  # Example MAC address

    # Construct the Magic Packet
    magic_packet = b'\xFF' * 6 + target_mac * 16  # 6 bytes of 0xFF followed by 16 repetitions of MAC address

    # Broadcast address (use the broadcast address of your network)
    # This might vary depending on your network setup. Common ones are '255.255.255.255' or '192.168.1.255'
    broadcast_address = '192.168.1.255'
    port = 9  # Default port for Wake-on-LAN is 9

    # Send the Magic Packet
    print("Sending Magic Packet...")
    sock.sendto(magic_packet, (broadcast_address, port))
    print("Magic Packet Sent!")

    # Clean up and close the socket
    sock.close()


def write_encoder_pos_display(encoder_value): # Update encoder position text
    encoder_pos.text = encoder_value  

def write_encoder_button_display(button_pressed):    # Update button state text
    encoder_button.text = f"Button: {button_pressed}"

def write_compsel_state(position): # uses comselect function to define selected computer and writes to variable on display
    slct.text= compselect(position)

def compselect(position):
    if position == 1:
        return "Desktop"
    if position == 2:
        return "FW Laptop"
    if position == 3:
        return "Lenovo Laptop"
    else:
        return "no stored value"
    
seesaw = seesaw.Seesaw(i2c, addr=0x36) # tells seesaw what the address and bus of the encoder is

seesaw.pin_mode(24, seesaw.INPUT_PULLUP)  # Configure seesaw pin used to read knob button presses
button = digitalio.DigitalIO(seesaw, 24)  # The internal pull up is enabled to prevent floating input

button_held = False # gives default value for button held

encoder = rotaryio.IncrementalEncoder(seesaw)
last_position = None

while True:
    
    position = -encoder.position # negate the position to make clockwise rotation positive

    if position != last_position:
        last_position = position
        print("Position: {}".format(position))
        write_encoder_pos_display("{}".format(position))
        write_compsel_state(position)
        if position == -20: #clears all messages from display and stops program when encoder reaches negitive 20
            for i in range(3):
                splash.pop()
            sleep(1)
            clear_unlock_display()
            break

    if not button.value and not button_held: # checks if button is pressed and if it is being continualy pressd
        button_held = True
        print("Button pressed")
        write_encoder_button_display("Pressed")

    if button_held == True:     # if the button is held for any length of time (pressed)0 then wake selected device
        if compselect(position) == "Desktop":
            WoL_Desktop(DESKTOP_MAC_ADDR)

    if button.value and button_held: # returns false when button is no longer being pressed
        button_held = False
        print("Button released")
        write_encoder_button_display("Not Pressed")
