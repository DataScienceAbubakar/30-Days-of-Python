# Level 1

def filter_list():
    numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
    return [x for x in numbers if x <= 0]


def flatten_list():
    list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
    return [x for sub in list_of_lists for sub2 in sub for x in sub2]


def generate_list_of_tuples():
    list_of_tuples = []
    for i in range(11):
        list_of_tuples.append((i, i ** 0, i ** 1, i ** 2, i ** 3, i ** 4, i ** 5))
    return list_of_tuples


def flatten_list_of_tuples():
    countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
    return [[sub2[0].upper(), sub2[0].upper()[:3], sub2[1].upper()] for sub in countries for sub2 in sub]


def list_to_list_dict():
    countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
    countries = [[sub2[0].upper(), sub2[1].upper()] for sub in countries for sub2 in sub]
    countries = [x for sub in countries for x in sub]
    keys = ["country", "city"]
    return [{keys[0]: countries[idx], keys[1]: countries[idx + 1]} for idx in range(0, len(countries), 2)]


def concatenate_list():
    names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
    conc = [x for sub in names for sub2 in sub for x in sub2]
    return [conc[i] + ' ' + conc[i + 1] for i in range(0, len(conc), 2)]


slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)
y_intercept = lambda x1, y1, x2, y2: y1 - slope(x1, y1, x2, y2) * x1
