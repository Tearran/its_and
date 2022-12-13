#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Copyright (c) 2022 Joseph Turner (Tearran) & contributors

import os, sqlite3
i2c_URL=os.path.dirname(__file__)+'/db/sqlite.db'

conn = sqlite3.connect(i2c_URL)

c = conn.cursor()
c.execute("SELECT * FROM its_i2cList")
rows = c.fetchall()

for row in rows:
    if row[6] != "URL not found":
        print('''
<tspan class="data headline" x="0" dx="0" dy="35">'''+str(row[1])+'''</tspan>
<a href="'''+row[6]+'''" target='_blank'>
<tspan class="data headline" dx="0" dy="0">'''+str(row[3])+'''</tspan>
</a>''') 
    
    else:
        pass                                                    
                                       
conn.close
