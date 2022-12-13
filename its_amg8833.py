#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Copyright (c) 2022 Joseph Turner (Tearran) & contributors


import time
from lib.amg8833 import AMGGridEye

# ini amg8833 lib
sensor = AMGGridEye()
#sensor.reset_flags_and_settings()
#time.sleep(.1)
#sensor.set_fps_mode(AMGGridEye.FPS_10_MODE)
get_pix= sensor.update_pixel_temperature_matrix()
try:  
#while(True):
  #update temperature
    get_pix
#    time.sleep(.1)
    
finally:
#    print(sensor.get_pixel_temperature_matrix())
    #print(str(round(sensor.get_thermistor_temperature(), 0))) 
    arr = sensor.get_pixel_temperature_matrix()
    for row in arr:
        print('''
<tspan class="data headline" x="0" dx="0" dy="35">'''+str(row)+'''</tspan>
''') 
#        print(row)