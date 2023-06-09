"""
Домашнее задание №1
Функции и структуры данных
"""
import math


def power_numbers(*numbers):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [number ** 2 for number in numbers]

# filter types
ODD = "odd" 
EVEN = "even"
PRIME = "prime"


def is_prime(num):
    if num == 1:
        return num == 2
    if num % 2 == 0:
        return num == 2
    d = 3
    while d * d <= num and num % d != 0:
        d += 2
    return d * d > num


def filter_numbers(list_numbers,filter):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)
clear
    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    if filter == ODD:
        return [number for number in list_numbers if number % 2 != 0]
    elif filter == EVEN:
        return [number for number in list_numbers if number % 2 == 0]
    elif filter == PRIME:
        return [number for number in list_numbers if is_prime(number)]
