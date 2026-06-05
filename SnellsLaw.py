"""
Light Refraction Calculator (Snell's Law)

This script computes the angle of refraction using Snell's Law. It includes 
a command-line interface, a material reference list, and degree formatting.

Functions:
- find_angle_of_refraction(n1, n2, aenter): Computes the refraction angle.
  * I/O: (float: n1, float: n2, float: angle) -> str (Formatted as D°M'S")
  * Raises: ArcsinValueError if the calculation is mathematically invalid.
"""

import numpy as np
import os
import time

def ClearScreen():
    print("\033[H\033[J", end="")

class ArcsinValueError(Exception):
    pass

def print_index():
    ClearScreen()
    print("""Vacuume: 1
Air: 1.0003 (usually rounded to 1)
CO2: 1.0004 (usually rounded to 1)
Water: 1.33... (usually rounded to 1.33)
Ethanol (Alcohol): 1.361
Glycerol: 1.473
Olive Oil: 1.470
Ice: 1.310:
Fluorite: 1.434
Glass: 1.5 (varies from type-to-type but commonly 1.5)
Diamond: 2.417""")
    input("'ENTER' to continue")

def print_instructions():
    ClearScreen()
    print("""ALWAYS PUT THE REFRACTIVE INDEX OF THE INITIAL MEDIUM FIRST, for example, if light is entering
FORM AIR (n = 1) into water (n = 1.33), you input '1 1.33 (and then the angle of incidence here)', it will
probably return a long ahh decimal, the full value is the angle, the decimals are the extras.""")
    input("'ENTER' to continue")

def find_angle_of_refraction(n1, n2, aenter):
    """args: refractive index of medium 1(int),
       refractive index of medium 2(int),
       angle of incidence(int).
       
       returns angle of refraction(int)"""
    thing = np.degrees(np.arcsin(n1 * np.sin(np.radians(aenter)) / n2))

    if np.isnan(thing):
        raise ArcsinValueError
    
    random_sign_thing = '"'
    d = int(thing)
    m = int((abs(thing) - abs(d)) * 60)
    s = round(((abs(thing) - abs(d)) * 60 - m) * 60, 1)

    while s >= 60 or m >= 60:
        if s >= 60:
            m += 1
            s -= 60
        if m >= 60:
            m -= 60
            d += 1

    return(f"{d}°{m}'{s}{random_sign_thing}")

if __name__ == "__main__":
    while True:
        ClearScreen()
        print("input '@index' for a list of common refractive indexes, and '@instruction' for instructions")
        print("-------------------------------------------------------------------------------------------")
        user_input = input("Input in this format: 'n1 n2 angleofincidence', e.g. 1 1.33 40:").lower().split()
        start = time.time()
        if len(user_input) == 0:
            continue
        elif user_input[0] == "@index":
            print_index()
            continue
        elif user_input[0] == "@instruction":
            print_instructions()
            continue
        
        else:
            try:
                ClearScreen()
                print(find_angle_of_refraction(float(user_input[0]), float(user_input[1]), float(user_input[2])))
                print(f"Runtime: {time.time() - start} seconds")
                input("'ENTER' to continue")
            except ArcsinValueError:
                input("Invalid Angles, math has a limit!")
            except:
                input("Invalid Input!") 
