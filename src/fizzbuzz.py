#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FizzBuzz - Clássico da programação
Desenvolvido por Bruno com ajuda do Otimus (IA)
"""

# Loop principal do FizzBuzz
for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)