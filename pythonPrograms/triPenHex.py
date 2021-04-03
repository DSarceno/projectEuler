#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#
# @Author: Diego Sarceno
# Date: 11.12.2020
#
#
#
# Problem 45 of Project Euler

'''este programa encuentra los numeros que son triangulares, pengatonales
y exagonales al mismo tiempo'''

import functions as fun

count = 0
num = 0
while True:
    tr = num*(num + 1)/2
    if fun.pentagonalN(tr) and fun.hexagonalN(tr):
        print(tr)
        count += 1
        if count == 5:
            break
    num += 1
