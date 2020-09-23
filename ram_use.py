#!/usr/bin/env python3

from openrgb import OpenRGBClient
from openrgb.utils import RGBColor, DeviceType

import psutil

client = OpenRGBClient()
ram = client.get_devices_by_type(DeviceType.DRAM)

while True:
    ram_use = int(psutil.virtual_memory()[2])
    loops = int((ram_use / 20) + 1)
    colour = 5 - loops
                
    for i in range(4, -1, -1):
        if loops > 0:
            ram[1].leds[x].set_color(RGBColor.fromHSV(colour * 24,100,100))
            ram[3].leds[x].set_color(RGBColor.fromHSV(colour * 24,100,100))
            ram[0].leds[x].set_color(RGBColor.fromHSV(colour * 24,100,100))
            ram[2].leds[x].set_color(RGBColor.fromHSV(colour * 24,100,100))
        else:
            ram[1].leds[x].set_color(RGBColor(0, 0, 0))
            ram[3].leds[x].set_color(RGBColor(0, 0, 0))
            ram[0].leds[x].set_color(RGBColor(0, 0, 0))
            ram[2].leds[x].set_color(RGBColor(0, 0, 0))
        loops = loops - 1
