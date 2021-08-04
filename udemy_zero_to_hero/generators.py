# Problem 1

# def gensquares(n):
#     for x in range(n):
#        yield  x ** 2

# for x in gensquares(10):
#     print(x)

# Problem 2

# from random import randint

# def rand_num(low, high, n):
#     for n in range(n):
#         random = randint(low, high)
#         print(random)

# print(rand_num(1, 10, 12))

# Problem 3

s = 'hello'
s = iter(s)
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))