#!/usr/bin/env python3

from openrgb import OpenRGBClient
from openrgb.utils import RGBColor, DeviceType

import psutil

client = OpenRGBClient()

cooler = client.get_devices_by_type(DeviceType.COOLER)[0]
cpu_led = cooler.zones[2].leds[0]

while True:
    current_temp = int(psutil.sensors_temperatures()['k10temp'][-1].current)

    min_temp = 35
    max_temp = 65

    min_hue = 0         #Red
    max_hue = 120       #Green
    
    step = max_hue / (max_temp - min_temp)
    
    offset = current_temp - min_temp
    current_hue = max_hue - (offset * step)

    if current_hue < min_hue:
        current_hue = min_hue

    cpu_led.set_color(RGBColor.fromHSV(current_hue, 100, 100))
