import math
import os
import random
import re
import sys


def input_values():
    while True:
        user_values = input("Enter integers:")
        elements = user_values.split()
        if len(elements) == 5:
            return [int(x) for x in elements]
        else:
            print("Please re-enter")

def min_max_sum(arr):
    arr.sort()
    min_sum = sum(arr[:-1])
    max_sum = sum(arr[1:])
    return min_sum, max_sum


if __name__ == '__main__':
    numbers = input_values()
    min_result, max_result = min_max_sum(numbers)
    print(f"{min_result} {max_result}")