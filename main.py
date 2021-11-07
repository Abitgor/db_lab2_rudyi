from db_processing import *


def first_query_data():
    result = query_result(1)
    data = {
        'Battlegrounds': [i[0] for i in result],
        'Alliance Players': [i[1] for i in result],
    }
    return data


def second_query_data():
    result = query_result(2)
    data = {
        'Class': [i[0] for i in result],
        'Players': [i[1] for i in result],
    }
    return data


def third_query_data():
    result = query_result(3)
    data = {
        'Class': [i[0] for i in result],
        'Kills': [i[1] for i in result],
    }
    return data


def print_result(data):
    keys = list(data.keys())
    print("{:<25} {:<10}".format(keys[0], keys[1]))
    print("_" * 35)
    for i in range(len(data[keys[0]])):
        print("{:<25} {:<10}".format(data[keys[0]][i], data[keys[1]][i]))
    print('\n')


if __name__ == '__main__':
    print("First query")
    print_result(first_query_data())
    print("Second query")
    print_result(second_query_data())
    print("Third query")
    print_result(third_query_data())
