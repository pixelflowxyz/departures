import data
from datetime import datetime, timedelta

southbound = "brijmjt"  # THELEVEL_P
northbound = "bridtpm"  # THELEVEL_I


def getdata():
    return data.combine_two_stops(northbound, southbound)


def round_to_nearest_minute(time):
    # Calculate the number of seconds since the start of the minute
    seconds = time.second + time.microsecond / 1_000_000
    # Determine if we need to round up or down
    if seconds >= 30:
        # Round up
        time += timedelta(minutes=1)
    # Remove the seconds and microseconds
    return time.replace(second=0, microsecond=0)


def timeuntil(time):
    time = round_to_nearest_minute(time)
    now = round_to_nearest_minute(datetime.now())
    time_diff = time - now
    minutes_until = int(time_diff.total_seconds() // 60)
    if minutes_until < 1:
        return "Now"
    elif minutes_until == 1:
        return f"{minutes_until} min"
    else:
        return f"{minutes_until} mins"


def currenttime():
    return str(datetime.now().strftime("%H:%M"))
