import random

MAX_SIZE = 100


def generate_random_list(size):
    result = []
    for i in range(size):
        result.append(random.randint(1, MAX_SIZE))
    return result
