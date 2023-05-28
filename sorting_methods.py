# different lambda functions for comparing elements in an array
# increasing numbers
import pygame
from colors import *

from main import draw_elements

ascending_numbers = lambda first, second: first <= second
# decreasing numbers
descending_numbers = lambda first, second: first >= second


# sorts a given list of numbers based on the given criterion using Bubble Sort and updates it step by step
def bubble_sort(app, given_list, criterion):
    for i in range(len(given_list)):
        for j in range(len(given_list) - 1):
            if not criterion(given_list[j], given_list[j + 1]):
                given_list[j], given_list[j + 1] = given_list[j + 1], given_list[j]
                app.set_list(given_list)
                draw_elements(app, {j: GREEN, j + 1: RED})
                yield True
    return given_list


# sorts a given list of numbers based on the given criterion using Insertion Sort and updates it step by step
def insertion_sort(app, given_list, criterion):
    for i in range(1, len(given_list)):
        j = i
        while not criterion(given_list[j - 1], given_list[j]) and j > 0:
            given_list[j - 1], given_list[j] = given_list[j], given_list[j - 1]
            app.set_list(given_list)
            draw_elements(app,  {j - 1: GREEN, j: RED})
            yield True
            j = j - 1
    return given_list


# sorts a given list of numbers based on the given criterion using Selection Sort and updates it step by step
def selection_sort(app, given_list, criterion):
    for i in range(len(given_list) - 1):
        crt_extreme_index = i
        for j in range(i + 1, len(given_list)):
            if not criterion(given_list[crt_extreme_index], given_list[j]):
                crt_extreme_index = j
        given_list[i], given_list[crt_extreme_index] = given_list[crt_extreme_index], given_list[i]
        app.set_list(given_list)
        draw_elements(app, {i: GREEN, crt_extreme_index: RED})
        yield True
    return given_list