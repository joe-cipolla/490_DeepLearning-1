"""
Adds "noise" to a given array by randomly flipping bits on the array.
Returns a new Letter object.
"""
from random import random
from .Letter import Letter

def add_noise(all_letters, noise_percent=0, num_noisy_nodes=0):
    i = 0
    while i < (num_noisy_nodes - 1):
        letter = random.choice(all_letters)
        letter_array = letter.array
        p = 0
        while (p / float(len(letter_array))) < noise_percent:
            letter_array[random.choice(range(len(letter_array)))] = random.choice(range(2))
            p += 1
        letter.array = letter_array
        i += 1
    return all_letters
