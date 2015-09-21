#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Vamos a programar una calculadora

import sys

def main():
    pass

def suma (sum1, sum2):
    return sum1 + sum2

if __name__ == "__main__":
    try:
        num1 = int (sys.argv[2])
        num2 = int (sys.argv[3])
    except ValueError:
        sys.exit("Tienen que ser números enteros")
    print (suma(num1, num2))

