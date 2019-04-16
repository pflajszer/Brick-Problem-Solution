#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 17:11:23 2019

The program calculates a maximum load that can be placed on top of the given wall.

@author: Pawel Flajszer
"""

# Import modules:
# ======================================================================================================================

import re
import sys

# Functions:
# ======================================================================================================================

def check_args():
    """ Check the number of command line arguments. Return error if not equals 3. """
    if len(sys.argv) != 3:
        raise TypeError(f"This app takes exactly 3 arguments ({len(sys.argv)} given). \
Usage: python app.py text_file.txt input_position")

def check_extension():
    """ Check if first argument ends with the right extension (*.txt) """
    if sys.argv[1][-4:] != '.txt':
        raise TypeError("The text file has to have the right extension (*.txt)")

def check_input_position(wall):
    """ Validate the input position. """
    if int(sys.argv[2]) > len(wall[0]):
        raise ValueError("The input position is larger than the lenght of the wall (index 0 is position 1).")
    if int(sys.argv[2]) < 1:
        raise ValueError("The input position must be a positive integer.")
    if int(sys.argv[2]) < len(wall)-1 or int(sys.argv[2]) > len(wall[0]) - (len(wall)-1):
        raise ValueError("The calculation cannot touch the side wall for the accuracy purposes. \
Place the input position closer to the middle of the wall.")

def read_file(file):
    """ Open given file and returns the content as a string """
    with open(file) as f:
        wall = f.read()
    return wall

def check_file_format(wall):
    """ Using regex check if the string in the text file has the right formatting. """
    if re.match('^-*\n\| \d{3} \|', wall) is not None:
        return True

def create_wall(file):
    """ Create an iterable list of lists out of the single string read from the file. """
    wall = read_file(file)  
    if check_file_format(wall):                                 
        wall = wall.split('\n')                                 # Split a wall into rows on newline char
        for row in range(0, len(wall)):                         
            wall[row] = re.split('[^\d{3}]', wall[row])         # Split wall into rows of 3 digits using regex
            wall[row] = list(filter(None, wall[row]))           # Remove empty strings from each row
        wall = [row for row in wall if row != []]               # Remove empty lists from rows
        return wall

def divide_bricks(pyramid):
    """ Divide every bricks' strenght rating by 990 to prepare them for multiplication. """
    for row in pyramid:
        for i in range(0, len(row)):
            row[i] /= 990


def create_pyramid(wall, ip):
    """ Shorten the rows to relevant values - integers in range 800-999 under the initial position brick."""
    ni = ip        # Negative index
    pi = ip+1      # Positive index
    for row in range(0, len(wall)):
        if row % 2 == 0 and row != 0:
            pi += 1
        elif row != 0:
            ni -= 1
        wall[row] = wall[row][ni:pi]
        wall[row] = list(map(int, wall[row]))
    return wall

def choose_weaker_path(pyramid, r, b):
    """ Look at two values directly above, and multiply the weaker one. """
    if r != 1:
        temp = []
        temp.append(pyramid[r][b] * pyramid[r-1][b-1])
        temp.append(pyramid[r][b] * pyramid[r-1][b])
        temp.sort()
        pyramid[r][b] = temp[0]

def left_edge(pyramid, a):
    """ Calculate the next left-edged value. """
    pyramid[a][0] = pyramid[a][0] * pyramid[a-1][0]

def right_edge(pyramid, b):
    """ Calculate the next right-edged value. """
    pyramid[b][-1] = pyramid[b][-1] * pyramid[b-1][-1]

def row_calculations(pyramid, r):
    """ Perform all calculations for the current row. """
    left_edge(pyramid, r)
    for i in range(1,r):
        choose_weaker_path(pyramid, r,i)
    right_edge(pyramid, r)


# Main:
# ======================================================================================================================

def main():

    check_args()
    check_extension()
    file = sys.argv[1]
    input_pos = (int(sys.argv[2])) - 1
    results = []
    counter = 0
    wall = create_wall(file)
    check_input_position(wall)
    pyramid = create_pyramid(wall, input_pos)
    divide_bricks(pyramid)

    # Main loop to find the weakest possible path.
    for i in range(1, len(pyramid)):
        row_calculations(pyramid, i)

    pyramid[-1].sort()
    print(f'{pyramid[-1][0]:.9f}')

# ======================================================================================================================

if __name__ == '__main__':
    main()