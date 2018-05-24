# Espmomether
Thermomether/Hygromether mythopython script for ESP-32 and ESP-8266 running Micropython using DHT22 and SSD1306

## Installation
Look at the values at the begining of the file and change them according to your pins setup and your display. My code works best for 128x64 SSD1306 oled displays using i2c. If you are using something else, you will need to make more modifications.

The default pin setup is for ESP-32 boards:
Dht data line : IO-33
SSD1306 SCL : IO-22
SSD1306 SDA : IO-21

After that's taken care of, follow the instruction for the dependencies and then transfer Espmomether.py to your board as main.py. If you don't know how to transfer files to your files, I recommend Adafruit-Ampy. If you are using Lobo Micropython, use the espmometer_lobo.py file instead.

## Dependecies
### SSD1306 Micropython Module
To get the script working on your device, you will need to be assured that you have the SSD1306 module for OLED displays on your board. You can skip this step if you are using Lobo Micropython as the ssd1306 is already implemented in this version. If you are using the official Micropython, you can grab Adafruit's Micropython driver for SSD1306 displays here : https://github.com/adafruit/micropython-adafruit-ssd1306, and put it on your board. 

### Fonts

Since, I cannot distribute the fonts I'm using, you will need to do some work. You will need to get Peter Hinch's Python3 script font_to_py.py here https://github.com/peterhinch/micropython-font-to-py and put it on your computer. (You will also need the writer.py file in the respository, but I'll get back to it later). Be sure to get the Freetype library and its Python bindings on your machine as explained here: https://github.com/peterhinch/micropython-font-to-py/blob/master/FONT_TO_PY.md

#### Inky Thin Pixels
You can download the .ttf file here: http://www.fontspace.com/chequered-ink/inky-thin-pixels.
open the terminal, change it to the location where you downloaded the ttf file and type:
```
font_to_py.py 'Inky Thin Pixels.ttf' 32 inkythin.py
```
It's possible that you have to type 'python' or 'Python3' in front of the command.
#### VCR OSD Mono
You can download the ttf here : https://www.dafont.com/fr/vcr-osd-mono.font.
Open the terminal, change it to the location where you downloaded the ttf file and type:
```
font_to_py.py VCR_OSD_MONO_1.001.ttf 21 vcr_osd.py
```
Again, you might have to write 'python' or 'python3' before the code.

### The Writer Class by Peter Hinch
Back to our Font to Py repository, we will have to copy writer.py (https://github.com/peterhinch/micropython-font-to-py/blob/master/writer.py) to the board. This class is used to display the costom fonts that we converted to py files. 
Adafruit's SSD1306 driver doesn't allow us to use costom fonts, so this is the best workaround. Lobo micropython already has a writer class, but it's not compatible with the font_to_py script for now, so I suggest changing the name of the file to writa.py on this version.

## Difference with Lobo Python
Lobo Micropython is more efficient for coding. The main reason why I use it is because it's the only version of micropython that's compatible with Sd cards on the ESP32. This version of espmometer blinks the esp32's internal LED whenerver ther's an error.
