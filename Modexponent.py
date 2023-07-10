#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 15:28:13 2023

@author: cornelius
"""

import math

a = int(input("Enter the first number "))
b = int(input("Enter exponent "))
n = int(input("Enter the modulus range "))
# calculate the modulus of an exponential
def modular_exponent(a, b, n):
    result = 1
    for i in range(0, b):
        result *= a
        result %= n

    return result


# print(modular_exponent(3, 340, 341))


#print(bin(73))


def fast_exponent(a, b, n):
    binary_list = []
    binary_string = str(bin(b))
    for i in range(2, len(binary_string)):
        binary_list.append(binary_string[i])

    binary_list.reverse()

    # print(binary_list)

    # calculate squares
    square_list = []
    square = a
    square_list.append(a)
    for i in range(0, len(binary_list) - 1):
        square = (square ** 2) % n
        square_list.append(square)

    # print(square_list)

    # Multiply the squares
    product = 1
    binary_squares = list(zip(binary_list, square_list))
    print(binary_squares)

    for element in binary_squares:
        if element[0] == '1':
            product *= element[1] % n

    return product % n


print(fast_exponent(a, b, n))












