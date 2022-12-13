#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Copyright (c) 2022 Joseph Turner (Tearran) & contributors


from lib.mlx90614 import MLX90614
import sys

thermometer_address = 0x5a
thermometer = MLX90614(thermometer_address)

print('''<tspan class="data headline" x="0" dx="0" dy="35">'''
+str(round(thermometer.get_amb_temp() * 1.8 + 32, 1))+
'''</tspan>''')

print('''<tspan class="data headline" x="0" dx="0" dy="35">'''
+str(round(thermometer.get_obj_temp()* 1.8 + 32, 1))+
'''</tspan>''')

print('''<tspan class="data headline" x="0" dx="0" dy="35">'''
+str(thermometer.get_amb_temp())+
'''</tspan>''')

print('''<tspan class="data headline" x="0" dx="0" dy="35">'''
+str(thermometer.get_obj_temp())+
'''</tspan>''')
