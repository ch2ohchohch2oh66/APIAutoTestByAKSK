# -*- coding: utf-8 -*-
# Author: Andy Freeman
# Date: 2024/11/1
# Description: Keep Hungry Keep Foolish
import random
import string


def generate_random_string(length=10):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(population=characters, k=length))

def generate_random_alpha_string(length=10):
    alpha_characters = string.ascii_letters
    return ''.join(random.choices(population=alpha_characters, k=length))

def generate_random_digit_string(length=10):
    digit_characters = string.digits
    return ''.join(random.choices(population=digit_characters, k=length))


def find_value_by_key(json_data, target_key):
    if isinstance(json_data, dict):
        for key, value in json_data.items():
            if key == target_key:
                return value
            elif isinstance(value, (dict, list)):
                result = find_value_by_key(value, target_key)
                if result is not None:
                    return result
    elif isinstance(json_data, list):
        for item in json_data:
            result = find_value_by_key(item, target_key)
            if result is not None:
                return result
    return None
