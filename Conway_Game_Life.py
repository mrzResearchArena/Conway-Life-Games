# Rafsanjani Muhammod
# Problem : Conway's Game of Life

from math import *
from numpy import *
from pandas import *


def isValid(row, column):
    if (row >= 1 and row <= 9) and (column >= 1 and column <= 9):
        return True
    else:
        return False


def adjacent(box, row, column):
    if box[row, column] == 1:
        C = 0
    else:
        C = 1

    i = row - 1
    while i <= row + 1:
        j = column - 1
        while j <= column + 1:
            if isValid(i, j):
                if box[i, j] == 1:
                    C = C + 1
            j = j + 1
        i = i + 1

    return C - 1


def calculation(box, reserved):
    for i in range(1, 10, 1):

        for j in range(1, 10, 1):

            C = adjacent(box, i, j)

            if box[i, j] == 1:

                # print("({}, {}), C = {}".format(i, j, C))

                if (C == 2) or (C == 3):
                    reserved[i, j] = 1  # Remain population
                elif C < 2:
                    reserved[i, j] = 0  # Under population
                elif C > 3:
                    reserved[i, j] = 0  # Over population

            else:

                # print("({}, {}), C = {}".format(i, j, C))

                if C == 3:
                    reserved[i, j] = 1  # Reproduction

    return reserved


def isDead(myArray):
    for i in range(1, 10, 1):
        for j in range(1, 10, 1):
            if myArray[i, j] != 0:
                return False

    return True


def isHappy(pre, next):
    for i in range(1, 10, 1):
        for j in range(1, 10, 1):
            if pre[i, j] != next[i, j]:
                return False

    return True


def display(myArray):
    for column in range(1, 10, 1):
        if column == 1:
            print("   ", column, end="")
        else:
            if column == 2:
                print("", column, end=" ")
            else:
                print(column, end=" ")
    print()

    for i in range(1, 10, 1):
        print(i, end=" : ")
        for j in range(1, 10, 1):
            print(myArray[i, j], end=" ")
        print()

    print()

def main():

    box = zeros([10, 10], dtype=int)

    box[4, 5] = 1
    box[5, 5] = 1
    box[5, 6] = 1
    box[6, 4] = 1
    box[6, 6] = 1

    pre = zeros([10, 10], dtype=int)
    next = zeros([10, 10], dtype=int)

    pre[:, :] = box[:, :]
    next[:, :] = box[:, :]

    print("Generation # 0 :")
    display(box)

    C = 1
    while True:

        next = calculation(pre, next)

        print("Generation # {} :".format(C))
        display(next)

        if isDead(next):
            print("Dead ! at generation : {}".format(C-1))
            break
        else:
            if isHappy(pre, next):
                print("Happy ! at generation : {}".format(C-1))
                break

        pre[:,:] = next[:,:]

        C = C + 1


if __name__ == '__main__':
    main()

