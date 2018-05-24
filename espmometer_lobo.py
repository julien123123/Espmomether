import machine, ssd1306, time, vcr_osd, inkythin
from writa import Writer


d= machine.DHT(machine.Pin(33), machine.DHT.DHT2X)
i2c = machine.I2C(1, sda=21, scl=22)
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
oled.fill(0)
oled.show()
led = machine.Pin(2, machine.Pin.OUT)

while True:
    d.read()
    time.sleep(0.5)
    result, temperature, humidity = d.read()
    if result == False:
        for i in range(5):
            led.value(1)
            time.sleep(.5)
            led.value(0)
        break
    oled.fill(0)
    itxt = Writer(oled, inkythin)
    vtxt = Writer(oled, vcr_osd)

    Writer.set_clip(True, True)
    Writer.set_textpos(0,0)

    itxt.printstring(str(temperature) + "'C\n")
    vtxt.printstring(str(humidity) + ' %')
    oled.show()
    time.sleep(10)
