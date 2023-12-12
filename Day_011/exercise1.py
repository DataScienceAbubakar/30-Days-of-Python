first_name = input ('enter first name')
last_name = input ('enter last name ')

def generate_full_name (first_name, last_name):
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print('Full Name: ', generate_full_name(first_name , last_name))