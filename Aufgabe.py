
# create a decorator called: chaosmachine
# it replaces all passed values with a random number between 1 and 100
# and then calls the original function

import random

def chaosmachine(func):
    def wrapper(*args, **kwargs):
        zufallszahl = (random.random()*100)
        result = func(zufallszahl)
        return result
    return wrapper


@chaosmachine
def double_value(my_number):
    return my_number*2


if __name__ == '__main__':
    print(double_value(2))