from functools import reduce
import sys

sys.path.append('data')
# noinspection PyUnresolvedReferences
from countries import country_list
# noinspection PyUnresolvedReferences
from countries_data import data
import pprint

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Level 1
'''If you already have a list of values and you want to do the exact same operation on each of the elements in the 
array and return the same amount of items in the list, in these type of situations it is better to use the map 
method. '''
'''If you already have list of values but you only want to have items in the array that match certain criteria, 
in these type of situations it is better to use the filter method. '''
'''If you already have list of values, but you want to use the values in that list to create something completely 
new, in these type of situations it is better to use the reduce method '''

'''A higher order function is a function that takes a function as an argument OR* returns a function.'''
'''A decorator in Python is (typically) an example of a higher-order function, but there are decorators that aren't (
class decorators**, and decorators that aren't functions), and there are higher-order functions that aren't 
decorators, for example those that take two required arguments that are functions. '''
'''A Closure is a function object that remembers values in enclosing scopes even if they are not present in memory.'''


def cube(num):
    return num ** 3


def vowel_name(name):
    if name[0] in 'aeiouAEIOU':
        return True
    return False


def sum_of_cubes(num1, num2):
    return num1 + num2


print(list(filter(vowel_name, names)))
print(list(map(cube, numbers)))
print(reduce(sum_of_cubes, list(map(cube, numbers))))

for i in countries:
    print(i)

for i in names:
    print(i)

for i in numbers:
    print(i)


# Level 2
def upper(string):
    return string.upper()


def square(num):
    return num ** 2


cap_countries = list(map(upper, countries))
square_nums = list(map(square, numbers))
upper_names = list(map(upper, names))


def land(string):
    if 'land' in string:
        return True
    return False


def six(string):
    if len(string) == 6:
        return True
    return False


def six_or_more(string):
    if len(string) >= 6:
        return True
    return False


def E(string):
    if string[0] == 'E':
        return True
    return False


print(list(filter(land, countries)))
print(list(filter(six, countries)))
print(list(filter(six_or_more, countries)))
print(list(filter(E, countries)))

print(list(filter(land, list(filter(six, countries)))))


def toString(string):
    return str(string)


def get_string_lists(arr):
    return list(map(toString, arr))


print(get_string_lists(numbers))


def sum2(x, y):
    return int(x) + int(y)


print(reduce(sum2, numbers))


def concatenate_countries(x, y):
    if x == "Estonia, Finland, Sweden, Denmark, Norway" and y == "Iceland":
        return x + ", and " + y
    else:
        return x + ", " + y


print(reduce(concatenate_countries, countries) + " are north European countries")

print(list(filter(land, country_list)))

keys = []
keys = [i[0] for i in country_list if i[0] not in keys]


def countCountry(csv1):
    return sum([True for i in country_list if i[0].startswith(csv1)])


vals = [countCountry(l) for l in keys]

print(dict(zip(keys, vals)))


def get_first_ten():
    return country_list[:10]


def get_last_ten():
    return country_list[-1:-11:-1]


# Level 3

pprint.pprint(sorted(data, key=lambda x: x['name']))
pprint.pprint(sorted(data, key=lambda x: x['capital']))
pprint.pprint(sorted(data, key=lambda x: x['population']))

total_languages_initial = []
for i in data:
    total_languages_initial.extend(i["languages"])
# noinspection DuplicatedCode
counts = {}
for i in total_languages_initial:
    counts[i] = counts.get(i, 0) + 1


def sort_dict_by_value(d, reverse=False):
    return dict(sorted(d.items(), key=lambda x: x[1], reverse=reverse))


counts = sort_dict_by_value(counts, True)
final_dict_1 = {}
for i in list(counts.items())[:10]:
    final_dict_1[list(i)[0]] = list(i)[1]
pprint.pprint(sorted(final_dict_1))

pprint.pprint(list(sorted(data, key=lambda x: x['population'], reverse=True))[:10])
