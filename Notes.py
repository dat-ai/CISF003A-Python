import functools as ft
import math
# Perfect-square number

our_string = "String_with_weird_underscores"

words = our_string.split("_")

other_words = []

for i in words:
    print(i)

print("_".join(words))

res = ft.reduce(lambda x, y: x + "_" + y, words, "python")
print(res[0:])


res2 = ft.reduce(lambda x, y: x + y, range(1, 2), 15)
print(res2)

res3 = ft.reduce(lambda x, y: x*y, range(1, 6), 1)
print(res3)

res4 = ft.reduce(lambda x, y: x + y, map(lambda x: x*x, range(1, 11)), 0)
print(res4)

res5 = sum([i*i for i in range(1, 11)])
print(res5)

# Predicates - function that returns true or false given an input


def is_odd(x): return x % 2 == 1


def is_perfect_square(x):
    return int(math.sqrt(x))**2 == x

filter_res = [i for i in range(1, 11) if is_odd(i)]    # list comprehension
print(filter_res)


filter_perfect_square = [i for i in range(1, 30) if is_perfect_square(i)]
print(filter_perfect_square)

filter_perfect_square2 = filter(lambda x: int(math.sqrt(x))**2 == x, range(1, 30))
print(list(filter_perfect_square2))

bool
