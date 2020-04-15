# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 12:53:17 2020

@author: DANIEL ALLI
"""
num=int(input("input any number :>>>  "))
if num % 3 == 0 and  num % 5 == 0:
    print("fizzbuzz")
if num % 3 == 0 :
    print("fizz")
if num % 5 == 0:
    print("buzz")
else :
    print(num)


