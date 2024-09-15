"""Generate the graphic for the display"""

from PIL import Image, ImageDraw, ImageFont
import busdata
import format

extrabold19 = ImageFont.truetype('fonts/Inter-ExtraBold.ttf', 19)
bold19 = ImageFont.truetype('fonts/Inter-Bold.ttf', 19)

black = 0
white = 255

width = 250
height = 112

busdata = format.getdata()

# for x in range(0,5):
#      print(f"{data[x][3]}  {data[x][0]}    {data[x][1]}  {format.timeuntil(data[x][2])}")


def truncate(destinput):
    if destinput == "Old Steine south":
        destinput = "Old Steine"
    if "Eastbourne" in destinput.split():
        destinput = "Eastbourne"
    left, top, right, bottom = bold19.getbbox(destinput)
    width = right - left
    trunc = destinput
    while width > 119:
        if trunc[-3:] == "...":
            trunc = trunc[:-3]
        trunc = trunc[:-1]
        trunc = f"{trunc}..."
        left, top, right, bottom = bold19.getbbox(trunc)
        width = right - left
        height = bottom - top       
    return trunc
    # if len(destinput) > 12:
    #     trunc = destinput[:10]
    #     return (f"{trunc}...")
    # else:
    #     return (destinput)
✨ added basic e-ink code



def generatebus():
    stop_name = "The Level"

    image = Image.new('1', (width, height), black)
    draw = ImageDraw.Draw(image)
    draw.rectangle(((0, 0), (250, 17)), fill=white)

    bus = Image.open('assets/bus.png')
    image.paste(bus, (3, 1))

    up = Image.open('assets/up.png')
    down = Image.open('assets/down.png')
    arrow = down

    draw.text((22, 2), stop_name, font=extrabold19,
              fill=black, anchor="lt")  # Title

    increment = 18
    start = 36

    for x in range(0, 5):
        if busdata[x][3] == "Northbound":
            arrow = up
        else:
            arrow = down
        route_number = busdata[x][0]
        route_dest = truncate(busdata[x][1])
        time = format.timeuntil(busdata[x][2])
        image.paste(arrow, (4, start-13+(increment*x)))
        # draw.text((10, start+(increment*x)+7), ns, font=bold19, fill=white, anchor="mm")
        draw.text((17, start+(increment*x)), route_number,
                  font=bold19, fill=white, anchor="ls")  # Route number
        draw.text((59, start+(increment*x)), route_dest, font=bold19,
                  fill=white, anchor="ls")  # Route destination
        draw.text((244, start+(increment*x)), time, font=bold19,
                  fill=white, anchor="rs")  # Route destination

    draw.text((244, 2), format.currenttime(),
              font=extrabold19, fill=black, anchor="rt")
    return image


