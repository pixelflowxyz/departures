import display
import time

from waveshare_epd import epd2in13_V4

epd = epd2in13_V4.EPD()
epd.init()
epd.Clear(0xFF)w

refresh_count = 0

force_full_update = 0

def eink(mode):
    if mode == "on":
        global refresh_count
        image = display.generatebus()
        display_image = epd.getbuffer(image)

        if force_full_update or refresh_count >= 10:
            epd.init(epd.FULL_UPDATE)
            epd.display(display_image)
            refresh_count = 1
        else:
            epd.init(epd.PART_UPDATE)
            epd.display_fast(display_image)
            refresh_count += 1
    
    if mode == "reset":
        epd.init()
        epd.Clear(0xFF)
        
while True:
    eink("on")
    time.sleep(10)
    