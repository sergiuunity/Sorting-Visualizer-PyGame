import pygame
import random


class SortingVisualizer:

    def __init__(self, given_width, given_height, given_list, given_sort_name, given_order, given_order_criterion,
                 given_sort_method):
        """This creates a new instance of the SortingVisualizer class."""
        self.__width = given_width
        self.__height = given_height
        self.__list = given_list
        self.__screen = pygame.display.set_mode((given_width, given_height))
        pygame.display.set_caption("Sorting Visualizer")
        self.__sort_name = given_sort_name
        self.__sort_method = given_sort_method
        self.__order = given_order
        self.__order_criterion = given_order_criterion

    def get_width(self):
        """Returns the width."""
        return self.__width

    def get_height(self):
        """Returns the height."""
        return self.__height

    def get_list(self):
        """Returns the list."""
        return self.__list

    def set_list(self, given_list):
        """Replace the current list with the given list."""
        self.__list = given_list

    def get_list_size(self):
        """Returns the size of the list of numbers."""
        return len(self.__list)

    def get_element_at_index(self, given_index):
        """Returns the element at the given index in the list."""
        return self.__list[given_index]

    def set_element_at_index(self, given_index, given_element):
        """Replace the element at the given index with the given one in the list."""
        self.__list[given_index] = given_element

    def get_screen(self):
        """Returns the screen."""
        return self.__screen

    def get_sort_name(self):
        """Returns the name of the currently used sort method."""
        return self.__sort_name

    def set_sort_name(self, given_sort_name):
        """Replace the current name of the sort with the given one."""
        self.__sort_name = given_sort_name

    def get_sort_method(self):
        """Returns the currently used sort method."""
        return self.__sort_method

    def set_sort_method(self, given_sort_method):
        """Replace the current sort method with the given one."""
        self.__sort_method = given_sort_method

    def get_order(self):
        """Returns the currently used sort order."""
        return self.__order

    def set_order(self, given_order):
        """Replace the current sort order with the given one."""
        self.__order = given_order

    def get_order_criterion(self):
        """Returns the currently used sort criterion."""
        return self.__order_criterion

    def set_order_criterion(self, given_order_criterion):
        """Replace the current sort criterion with the given one(as a lambda)."""
        self.__order_criterion = given_order_criterion
