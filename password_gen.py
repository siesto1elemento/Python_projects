import random

uppercase_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

lowercase_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', '|', ';', ':', ',', '.', '<', '>', '?', '/']

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']


my_list= []

def  password():
    random_uppercase = uppercase_list.random(1)
    random_lowercase = lowercase_list.random(1)
    random_special   = special_characters.random(1)
    random_number    = numbers.random(1)

    my_list.append(random_uppercase)
    my_list.append(random_lowercase)
    my_list.append(random_special)
    my_list.append(random_number)

    print(my_list)




