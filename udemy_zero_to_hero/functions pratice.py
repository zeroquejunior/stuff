# warmup 1
# def lesser_of_two_evens(x, y):
#     if x % 2 == 0 and y % 2 == 0:
#         return min(x, y)
#     elif x % 2 != 0 or y % 2 != 0:
#         return max(x, y)
#
# print(lesser_of_two_evens(2, 5))

# warmup 2
# def animal_crackers(x):
#     xx = x.split()
#     if xx[0][0].upper() == xx[1][0].upper():
#         return True
#     else:
#         return False
#
# print(animal_crackers('Cavalo camelo'))

# warmup 3
# def the_other_side_of_seven(x):
#     r = 7 - x
#     r = r * 2
#     r = r + 7
#     return r
#
#
# print(the_other_side_of_seven(12))

# leve 1-1
# def old_mcdonald(name=''):
#     if len(name) > 3:
#         return name[:3].capitalize() + name[3:].capitalize()
#
# print(old_mcdonald('macdonalds'))

# level 1-2
# def master_yoda(txt):
#     w = txt.split()
#     w.reverse()
#     return ' '.join(w)
#
# print(master_yoda('I am home'))

# leve 1-3
# def almost_there(n):
#     if n >= 90 and n <= 110:
#         return True
#     elif n >= 190 and n <= 210:
#         return True
#     else:
#         return False
#
# print(almost_there(209))

# level 2-1
# def laughter(pat, txt):
#     count = 0
#     for l in range(len(txt)-1):
#         if txt[l:l+len(pat)] == pat:
#             count = count + 1
#     return count
#
# print(laughter('ha', 'hahahaha'))

# level 2-2

# def paper_doll(txt):
#     x = 3
#     return ''.join([letter * x for letter in txt])
#
#
# print(paper_doll('Hello'))

# level 2-3
# from random import randint
# def blackjack(a, b, c):
#     x = a + b + c
#     if x <= 21:
#         return x
#     elif x > 21 and a == 11 or b == 11 or c == 11:
#         return x - 10
#     elif x > 21:
#         return 'BUST'
#
#
# a = randint(1, 11)
# b = randint(1, 11)
# c = randint(1, 11)
# print(a + b + c)
# print(blackjack(a, b, c))

# level 2-4
def summer_of_69(*num):
    numlist = list(num)
    rsum = []
    s = numlist.index(6, 0)
    e = numlist.index(9, 0)
    for n in range(s, e+1):
        rsum.append(numlist[n])
    print(s)
    print(e)
    print(rsum)
    return sum(numlist) - sum(rsum)


print(summer_of_69(4, 6, 8, 15, 9, 1, 5, 6, 8, 9))

