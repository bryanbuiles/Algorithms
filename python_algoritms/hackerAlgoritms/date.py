#!/usr/bin/python3
""" convertir hora pm am a hora militar """
import datetime


def timeConversion(s):
    hour = datetime.datetime.strptime(s, "%I:%M:%S%p")
    militarhour = hour.strftime("%H:%M:%S")
    print(type(hour))
    return (militarhour)


timeConversion("07:05:45PM")
