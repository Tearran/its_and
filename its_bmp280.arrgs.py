#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Copyright (c) 2022 Joseph Turner (Tearran) & contributors

import subprocess, sys, os
from lib.bmp_280 import BMP280

path=os.listdir(os.path.dirname(__file__))

bmp = BMP280(port=1, 
        mode=BMP280.FORCED_MODE, 
        oversampling_p=BMP280.OVERSAMPLING_P_x16, 
        oversampling_t=BMP280.OVERSAMPLING_T_x1,
        filter=BMP280.IIR_FILTER_OFF, 
        standby=BMP280.T_STANDBY_1000)

temp = str(bmp.read_temperature())
press = str(bmp.read_pressure())
tempf = str(float(temp) * 1.8 + 32)

if __name__ == "__main__":
    args = sys.argv
    # if no argument output all
    if len(args) < 2:
        sys.stdout.write('"'+tempf+'"')
    #if one argument output 
    # f for Fahrenheit 
    # c for Celsius
    # p for Pressure 
    # hpa hectopascal Pressure units
    
    elif len(args) >= 2:
        if args[1] == "-c":
            sys.stdout.write('"'+temp+'" ')
        elif args[1] == "-f":
            sys.stdout.write('"'+tempf+'" ')
        elif args[1] == "-p":
            sys.stdout.write('"'+press+'" ')
        elif args[1] == "-svg":
       
            sys.stdout.write('''
            <tspan class="data headline" x="0" dx="0" dy="35">'''+temp+'''</tspan>
            <tspan class="data headline" x="0" dx="0" dy="35">'''+press+'''</tspan>

            ''')
        elif args[1] == "-h" or "--help":
            sys.stdout.write('''
Useage: filename option
    -h or --help: display this help
    -f: Fahrenheit 
    -c: Celsius
    -p: for Pressure 
    -svg: hectopascal Pressure units

''') 
    sys.exit()       
