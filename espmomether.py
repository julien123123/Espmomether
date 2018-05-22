import machine
import dht, ssd1306
import time
from writer import Writer
import vcr_osd, inkythin

# These are the Pins used by the i2c bus of the ssd1306
scl = 22
sda = 21

# Height and width of the ssd1306
width = 128
height = 64

# pin used by the DHT22
dht_pin = 33

d = dht.DHT22(machine.Pin(dht_pin)) # DHT setup
i2c = machine.I2C(-1, machine.Pin(scl), machine.Pin(sda), freq=400000) # Oled screen setup
oled = ssd1306.SSD1306_I2C(width, height, i2c)

oled.fill(0) # clear the screen on boot
oled.show()

inky = Writer(oled, inkythin) # object to write using the Inky Thin Pixels font
vcr = Writer(oled, vcr_osd) # object to write using the VCR OSD Mono font

while True:
    d.measure() # Not recorded because it's always wrong
    time.sleep(0.5)
    d.measure()
    # storing the mesure in variables
    h = d.humidity()
    t = d.temperature()
    
    oled.fill(0) # clear the screen
    Writer.set_clip(True, True)
    Writer.set_textpos(0,0) # sets the origin of the text to 0,0
    # writing the dht measures to the screen
    inky.printstring(str(t) + "'C\n")
    vcr.printstring(str(h) + ' %')
    oled.show()
    time.sleep(10) #refreshes every 10 seconds
