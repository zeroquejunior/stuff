# Desafio 78
# lista = []
# ma = 0
# mi = 0
# for c in range(0, 4):
#     lista.append(int(input('Digite um valor:')))
# for i, v in enumerate(lista):
#     if v == max(lista):
#             ma = i
#     if v == min(lista):
#         mi = i
# print(f'O maior valor é o {max(lista)} na  {ma}º posição e o menor valor é o {min(lista)} na  {mi}º posição.')

# Desafio 79
# num = 0
# lista = []
# while True:
#     num = int(input('Digite um valor: '))
#     if num not in lista:
#         lista.append(num)
#         teste = int(input('Digite 00 para encerrar ou qualquer tecla para continuar:'))
#     else:
#         print('Valor já adicionado!')
#     if teste == 00:
#         break
# print(sorted(lista))

# Desafio 80
# lista = []
# r= 0
# for c in range(0, 4):
#     r = int(input('Digite um numero: '))
#     if c == 0 or r > lista[-1]:
#         lista.append(r)
#     else:
#         p = 0
#         while p < len(lista):
#             if r <= lista[p]:
#                 lista.insert(p, r)
#                 break
#             p = p + 1
# print(lista)

# Desafio 81
# lista = []
# while True:
#     lista.append(int(input('Digite um numero: ')))
#     e = ''
#     e = str(input('Quer continuar S/N: ')).lower()
#     if e == 'n':
#         break
# print(f'Foram digitados {len(lista)} numeros.')
# lista.sort(reverse=True)
# print(lista)
# if 5 in lista:
#     print(f'5 esta na lista, na posição {lista.index(5)}')
# else:
#     print('5 não esta na lista.')

# Desafio 82
# lista = []
# listap = []
# listai = []
# while True:
#     lista.append(int(input('Digite um valor: ')))
#     r = ''
#     r = str(input('Quer continuar S/N: '))
#     if r == 'n':
#         break
# for c in lista:
#     if c % 2 == 0:
#         listap.append(c)
#     else:
#         listai.append(c)
# print(f'Lista completa {lista}')
# print(f'Lista par {listap}')
# print(f'Lista impar {listai}')

# Desafio 83
# ex = str(input('Digite uma expressão: '))
# pa = []
# pf = []
# for sim in ex:
#     if sim == '(':
#         pa.append(sim)
#     elif sim == ')':
#         pf.append(sim)
# print(pa)
# print(pf)
# if len(pa) == len(pf):
#     print('Sua expressão esta correta.')
# else:
#     print('Sua expressão esta incorreta.')

