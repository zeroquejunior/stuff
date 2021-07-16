# Desafio 46
# from time import sleep
# for c in range(10, 1, -1):
#     print(c)
#     sleep(1)
# print(""" .* *.               `o`o`
#          *. .*              o`o`o`o      ^,^,^
#            * \               `o`o`     ^,^,^,^,^
#               \     ***        |       ^,^,^,^,^
#                \   *****       |        /^,^,^
#                 \   ***        |       /
#     ~@~*~@~      \   \         |      /
#   ~*~@~*~@~*~     \   \        |     /
#   ~*~@smd@~*~      \   \       |    /     #$#$#        .`'.;.
#   ~*~@~*~@~*~       \   \      |   /     #$#$#$#   00  .`,.',
#     ~@~*~@~ \        \   \     |  /      /#$#$#   /|||  `.,'
# _____________\________\___\____|_/______/_________|\/\___||______""")

# Desafio 47
# for n in range(1,51):
#     if n % 2 == 0:
#         print("Numero par: {}" .format(n))

# Desafio 48
# s = int()
# c = int()
# for i in range(1, 501, 2):
#     if i % 3 == 0:
#         c = c + 1
#         s = i + s
# print("A soma dos valores é: {}" .format(s))
# print("Foram somados {} numeros impares" .format(c))

# Desafio 49
# n = int(input("Type a number to get the times table: "))
# for t in range(1, 11):
#     print(n, "*", t, "=", n * t)

# Desafio 50
# s = int()
# for n in range(1, 7):
#     numbers = int(input("Type one number: "))
#     if numbers % 2 == 0:
#         s = numbers + s
# print("A soma dos numeros pares digitados é: {}" .format(s))

# Desafio 51
# t1 = int(input("Digite o 1ª termo da PA: "))
# r = int(input("Digite a razao da PA: "))
# a = int()
# for n in range(1, 11):
#     a = t1 + (n-1) * r
#     print(a, end=', ')

# Desafiom 52
# primo = int(input("Digite um numero para verificar se é primo: "))
# c = 0
# for n in range(1, primo + 1):
#     if primo % n == 0:
#         print('\033[34m', end=' ')
#         c = c + 1
#     else:
#       print('\033[31m', end=' ')
#     print('{}' .format(n), end=' ')
# print('\033[0mO numero {} foi divisivel {} vezes' .format(primo, c))
# if c == 2:
#     print('{} é um numero primo.' .format(primo))
# else:
#     print('{} não é um numero primo.' .format(primo))

# Desafio 53
# frase = str(input('Digite uma frase! Vamos checar se ela é um palindromo:')).lower()
# pal = frase[::-1]
# if pal == frase:
#     print('Sua frase é um palindromo')
#     print(pal)
# else:
#     print('Sua frase não é um palindromo')
#     print(pal)

# Desafio 54
# c = 0
# for n in range(1, 8):
#     year = int(input('Digite o ano de nascimento: '))
#     if 2021 - year >= 21:
#         c = c + 1
# print('{} pessoas são maior de idade' .format(c))
# print('Portanto {} pessoas são menores.' .format(7-c))

# Desafio 55
# list = []
# for n in range(1, 6):
#     weight = int(input('Digite o seu peso: '))
#     list.append(weight)
# print('O maior peso é {} e o menor peso é {}.' .format(max(list), min(list)))

# Desafio 56
# average_age = 0
# om = ''
# older_men = 0
# wl_20 = 0
# for n in range(1, 5):
#     name = str(input('Digite seu nome: '))
#     age = int(input('Digite sua idade: '))
#     gender = str(input('Digite o sexo [M/F]: ')).upper()
#     average_age = average_age + age
#     if n == 1 and 'M' in gender:
#         older_men = age
#         om = name
#     elif 'M' in gender and age > older_men:
#         older_men = age
#         om = name
#     elif 'F' in gender and age < 20:
#         wl_20 = wl_20 + 1
# print('The average age is {}' .format(average_age / 4))
# print('The oldest man is {} and he has {} years old.' .format(om, older_men))
# print('We have {} woman with less then 20 years old.' .format(wl_20))






