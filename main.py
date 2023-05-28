import pygame
import sys

from extra_functionalities import *
from sorting_visualizer import *
from colors import *
from sorting_methods import *


def start():
    pygame.init()

    is_sorting = False
    generator = None

    # creating the SortingVisualizer object
    width = 1280
    height = 720
    initial_list = generate_random_list(50)
    initial_sort_method = bubble_sort

    app = SortingVisualizer(width, height, initial_list, 'Bubble Sort', 'Ascending', ascending_numbers,
                            initial_sort_method)

    while True:
        # try to sort further if I'm currently sorting
        if is_sorting:
            try:
                next(generator)
            except StopIteration:
                is_sorting = False
        else:
            # drawing all the elements
            draw_elements(app)

        # checking for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # whenever we press a button on the keyboard
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    if app.get_list_size() > 50:
                        app.set_list(generate_random_list(app.get_list_size() - 1))
                elif event.key == pygame.K_UP:
                    if app.get_list_size() < 100:
                        app.set_list(generate_random_list(app.get_list_size() + 1))

                elif event.key == pygame.K_r:  # refresh the list
                    is_sorting = False
                    app.set_list(generate_random_list(app.get_list_size()))
                elif event.key == pygame.K_SPACE:  # sort the list
                    is_sorting = True
                    generator = app.get_sort_method()(app, app.get_list(), app.get_order_criterion())
                elif event.key == pygame.K_b:
                    app.set_sort_name('Bubble Sort')
                    app.set_sort_method(bubble_sort)
                elif event.key == pygame.K_i:
                    app.set_sort_name('Insertion Sort')
                    app.set_sort_method(insertion_sort)
                elif event.key == pygame.K_s:
                    app.set_sort_name('Selection Sort')
                    app.set_sort_method(selection_sort)

                elif event.key == pygame.K_a:
                    app.set_order('Ascending')
                    app.set_order_criterion(ascending_numbers)
                elif event.key == pygame.K_d:
                    app.set_order('Descending')
                    app.set_order_criterion(descending_numbers)


# Draw all the elements
def draw_elements(app, colors={}):
    clock = pygame.time.Clock()
    app.get_screen().fill(BACKGROUND_GREY)
    draw_list(app, colors)
    draw_text(app)
    # updating the screen
    pygame.display.update()
    clock.tick(60)


# Draw the current list on the screen
def draw_list(app, colors):
    # padding on left and right sides is 5%
    # padding on top is 40%
    rectangle_width = app.get_width() * 0.9 / app.get_list_size()
    rectangle_max_height = round(app.get_height() * 0.6)
    current_x = app.get_width() * 0.05

    # drawing each rectangle one by one
    for i in range(app.get_list_size()):
        current_rectangle_height = round(rectangle_max_height * (app.get_element_at_index(i) / 100))
        # rect(x, y, width, height)
        current_rectangle = pygame.Rect(current_x, app.get_height() - current_rectangle_height,
                                        rectangle_width * 0.995, current_rectangle_height)
        if i in colors:
            used_color = colors[i]
        else:
            used_color = BAR_COLORS[i % 3]
        pygame.draw.rect(app.get_screen(), used_color, current_rectangle)
        current_x += rectangle_width


# Draw all the text on the screen
def draw_text(app):
    # drawing all the text on the left side
    main_font_30 = pygame.font.Font('fonts/arial_narrow_7.ttf', 30)

    # draw the array size
    array_size_text_surface = main_font_30.render('Array Size: ' + str(app.get_list_size()), True, DARK_GREY)
    array_size_text_rectangle = array_size_text_surface.get_rect(topleft=(0.005 * app.get_width(),
                                                                          0.01 * app.get_height()))
    app.get_screen().blit(array_size_text_surface, array_size_text_rectangle)

    # draw the currently used sorting method
    sorting_method_surface = main_font_30.render(('Sort using: ' + app.get_sort_name() + ', ' + app.get_order()),
                                                 True, DARK_GREY)
    sorting_method_text_rectangle = sorting_method_surface.get_rect(topleft=(0.005 * app.get_width(),
                                                                             0.06 * app.get_height()))
    app.get_screen().blit(sorting_method_surface, sorting_method_text_rectangle)

    # draw the increase/decrease text
    modify_size_text_surface = main_font_30.render('Increase/Decrease Array Size: UP/DOWN', True, BABY_BLUE)
    modify_size_text_rectangle = modify_size_text_surface.get_rect(topleft=(0.005 * app.get_width(),
                                                                            0.11 * app.get_height()))
    app.get_screen().blit(modify_size_text_surface, modify_size_text_rectangle)

    # draw the regenerate text
    regenerate_text_surface = main_font_30.render('Regenerate Array: R', True, BABY_BLUE)
    regenerate_text_rectangle = regenerate_text_surface.get_rect(topleft=(0.005 * app.get_width(),
                                                                          0.16 * app.get_height()))
    app.get_screen().blit(regenerate_text_surface, regenerate_text_rectangle)

    # draw the sort text
    sort_text_surface = main_font_30.render('Sort: SPACE', True, BABY_BLUE)
    sort_text_rectangle = sort_text_surface.get_rect(topleft=(0.005 * app.get_width(),
                                                              0.21 * app.get_height()))
    app.get_screen().blit(sort_text_surface, sort_text_rectangle)

    # drawing all the text on the right side
    # draw the bubble sort text
    bubble_text_surface = main_font_30.render('Bubble Sort: B', True, BABY_BLUE)
    bubble_text_rectangle = bubble_text_surface.get_rect(topright=(0.990 * app.get_width(),
                                                                   0.01 * app.get_height()))
    app.get_screen().blit(bubble_text_surface, bubble_text_rectangle)

    # draw the insertion sort text
    insertion_text_surface = main_font_30.render('Insertion Sort: I', True, BABY_BLUE)
    insertion_text_rectangle = insertion_text_surface.get_rect(topright=(0.990 * app.get_width(),
                                                                         0.06 * app.get_height()))
    app.get_screen().blit(insertion_text_surface, insertion_text_rectangle)

    # draw the selection sort text
    selection_text_surface = main_font_30.render('Selection Sort: S', True, BABY_BLUE)
    selection_text_rectangle = selection_text_surface.get_rect(topright=(0.990 * app.get_width(),
                                                                         0.11 * app.get_height()))
    app.get_screen().blit(selection_text_surface, selection_text_rectangle)


    # draw the ascending/descending text
    ascending_descending_text_surface = main_font_30.render('Ascending/Descending: A/D', True, BABY_BLUE)
    ascending_descending_text_rectangle = ascending_descending_text_surface.get_rect(topright=(0.990 * app.get_width(),
                                                                                               0.16 * app.get_height()))
    app.get_screen().blit(ascending_descending_text_surface, ascending_descending_text_rectangle)


if __name__ == '__main__':
    start()
