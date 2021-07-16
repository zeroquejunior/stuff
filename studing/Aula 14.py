# Desafio 57
# gender = str(input('Type your gender as M or F:'))
# while gender != 'M' and gender != 'F':
#     gender = str(input('Wrong typing, please type your gender as M or F:'))
# print('Gender is {}' .format(gender))

# Desafio 58
# from random import randint
# rn = randint(0, 10)
# guess = int(input("Guess the number from 0 to 10:"))
# c = 0
# while guess != rn:
#     guess = int(input('Wrong guess, try again:'))
#     c = c + 1
# print('Good job you WIN with {} tries' .format(c+1))

# Desafio 59
# from time import sleep
# sum = 0
# times = 0
# greater = []
# n1 = int(input('Type number 1: '))
# n2 = int(input('Type number 2: '))
# c = 0
# while c != 5:
#     print(""" Escolha uma opção:
#     [1] somar
#     [2] multiplicar
#     [3] maior
#     [4] entrar novos numeros
#     [5] sair
#     """)
#     c = int(input('Choose one option: '))
#     if c == 1:
#         sum = n1 + n2
#         print('>>>>>A soma é igual a {} <<<<<'.format(sum))
#     elif c == 2:
#         times = n1 * n2
#         print('>>>>>A multiplicaçao é igual a {} <<<<<'.format(times))
#     elif c == 3:
#         greater.append(n1 and n2)
#         print('>>>>>O maior numero é {} <<<<<'.format(max(greater)))
#     elif c == 4:
#         n1 = int(input('Type number 1: '))
#         n2 = int(input('Type number 2: '))
#     elif c == 5:
#         print('>>>>>Finalizando... <<<<<')
#         sleep(1)
#
#     else:
#         print('>>>>>Opção invalida! <<<<<')
# print('>>>>>Programa finalizado <<<<<')

# Desafio 60
# fac = int(input('Digite um numero para saber se fatorial: '))
# c = fac
# r = 1
# while c >= 1:
#     print('{}' .format(c), end='')
#     print(' x ' if c > 1 else " = ", end='')
#     r = r * c
#     c = c - 1
# print(r)

# Desafio 61
# t1 = int(input("Digite o 1ª termo da PA: "))
# r = int(input("Digite a razao da PA: "))
# a = t1
# n = 1
# while n <= 10:
#     print(a, end=', ')
#     a = a + r
#     n = n + 1

# Desafio 62
# t1 = int(input("Digite o 1ª termo da PA: "))
# r = int(input("Digite a razao da PA: "))
# a = t1
# n = 1
# n2 = 10
# total = 0
# while n2 != 0:
#     total = total + n2
#     while n <= total:
#         print(a, end=', ')
#         a = a + r
#         n = n + 1
#     n2 = int(input('''
#     Quer continuar a sequencia de termos? Digite quantas vezes:
#     Se quiser finalizar digite >>>0<<< '''))
# print('FIM')

# Desafio 63
# n = int(input('Digite o primeiro numero para sequencia de fibonacci:  '))
# fb = 0
# fb1 = 0
# fb2 = 1
# fb3 = 0
# c = 0
# while c <= n:
#     fb3 = fb1 + fb2
#     print(fb, end=', ')
#     fb = fb1 + fb2
#     fb1 = fb2
#     fb2 = fb3
#     c = c + 1

# Desafio 64
# c = 0
# i = 0
# list = []
# while i != 999:
#     c = c + 1
#     i = int(input('Digite um valor  (999 vai parar): '))
#     list.append(i)
#     if i == 999:
#         list.remove(999)
#         print('Vc digitou {} numeros. O resultado da soma é {}.' .format(c - 1, sum(list)))

# Desafio 65
# c = 0
# i = 0
# q = 0
# list = []
# while q != 'exit':
#     c = c + 1
#     i = int(input('Digite um valor: '))
#     list.append(i)
#     print('Precione qualquer tecla para continuar ou digite (exit) para parar:')
#     q = input()
#     if q == "exit":
#         print('A media dos valores digitados é {:.2f}' . format(sum(list) / c))
#         print('O maior valor digitado é {}' .format(max(list)))
#         print('O maior valor digitado é {}'.format(min(list)))










