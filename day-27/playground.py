import random


# def add(*args):
#     su = 0
#     for n in args:
#         su += n
#     return su
#
# result = add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# print(result)


def calculate(n,**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    n += kwargs["add"]
    n *= kwargs["multiply"]

    print(n)



calculate(2, add=3, multiply=5)