#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#
# @Author: Diego Sarceno
# Date: 11.12.2020
#
#
#
# Problem 12 of Project Euler

'''Este programa encuentra el primer numero triangular con 500 divisores'''

import functions as fun

num = 1
while True:
    if fun.factors(fun.n_triang(num)) == 500:
        print(num)
        break
    num += 1
