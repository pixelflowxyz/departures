import display

from TP_lib import epd2in13_V2

DISPLAY = epd2in13_V2.EPD_2IN13_V2()
DISPLAY.init(DISPLAY.FULL_UPDATE)

refresh_count = 0

force_full_update = 0


def eink():
    global refresh_count
    image = display.generatebus()
    display_image = DISPLAY.getbuffer(image)

    if force_full_update or refresh_count >= 10:
        DISPLAY.init(DISPLAY.FULL_UPDATE)
        DISPLAY.displayPartBaseImage(display_image)
        refresh_count = 1
    else:
        DISPLAY.init(DISPLAY.PART_UPDATE)
        DISPLAY.displayPartial(display_image)
        refresh_count += 1