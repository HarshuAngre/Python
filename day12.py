

"""import random
import string

def  user_id_gen_by_user():
    count_of_char = int(input('enter the number of characters for the user id: '))
    id_count = int(input('enter the number of user ids to generate: '))
    
    characters = string.ascii_letters + string.digits

    for _ in range(id_count):
        user_id = ''.join(random.choice(characters) for _ in range(count_of_char))
        print(user_id)

user_id_gen_by_user()

import random

def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"rgb({r}, {g}, {b})"

print(rgb_color_gen())


def list_of_hex_colors(n):
    hex_colors = []
    for _ in range(n):
        hex_color = '#' + ''.join(random.choice('0123456789ABCDEF') for _ in range(6))
        hex_colors.append(hex_color)
    return hex_colors




def list_of_rgb_colors(n):
    rgb_colors = []
    for _ in range(n):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        rgb_colors.append(f"rgb({r}, {g}, {b})")
    return rgb_colors


color_type = input("Enter color type (hex/rgb): ")
n = int(input("Enter the number of colors to generate: "))
def generate_colors(color_type, n):
    if color_type == 'hex':
        return list_of_hex_colors(n)
    elif color_type == 'rgb':
        return list_of_rgb_colors(n)
    else:
        raise ValueError("Invalid color type. Use 'hex' or 'rgb'.")

print(generate_colors(color_type, n))

lst = [1, 2, 3, 4, 5]
def shuffle_list(lst):
    random.shuffle(lst)
    return lst
print(shuffle_list(lst))

def unique_numbers():
    return random.sample(range(10), 7)

print(unique_numbers())"""


