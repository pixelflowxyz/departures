import display
import time

from waveshare_epd import epd2in13_V4

epd = epd2in13_V4.EPD()
epd.init()
epd.Clear(0xFF)

refresh_count = 0

force_full_update = 0

def eink(mode):
    if mode == "on":
        global refresh_count
        image = display.generatebus()
        display_image = epd.getbuffer(image)

        if force_full_update or refresh_count >= 10:
            epd.init()
            epd.display(display_image)
            refresh_count = 1
        else:
            epd.init_fast()
            epd.display_fast(display_image)
            refresh_count += 1
    
    if mode == "reset":
        epd.init()
        epd.Clear(0xFF)
        
while True:
    eink("on")
    time.sleep(100)
    