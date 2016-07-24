def filter_custom(l, f):
    '''filter a list using a function
    return a new list that contains all the elements of e of l for which f(e) is True
    :param l: a list
    :param f: a function that takes on one argument and returns either True or False'''


    return [e for e in l if f(e)]


def map_custom(l ,f):

    '''map  a list using a function
    return a new list that applies f(e) for every element in l

    :param l: a list
    :param f: a function that takes on one argument and returns a value'''

    new_list = []
    for e in l:
        new_list.append(f(e))
    return new_list

def reduce_custom(l, x, starting_value):
    '''reduce a list using a reducer function and a starting value
    return a single value that applies f(v, e) for every e in l from left to right. the initial value for v should be starting_value, and subsequent values should be the previously calculated value from f(v, e)

:param l: a list
param f: a function that takes one argument and returns a value :para starting_value: the begginning value for the reducer function computation'''

    left_argument = starting_value
    for right_argument in l:
        left_argument = f(left_argument, right_argument)
    return left_argument




if __name__ == '__main__':
    l = [7,8,9]
    f = lambda x: x * 10
    print(map_custom(l, f))

print(filter_custom(l, f))
print(new_list_filt(l, f))
print(reduce_custom([1,2,3,17], f, 0))



