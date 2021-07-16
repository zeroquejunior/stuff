# Desafio 84
# dado = []
# info = []
# g = 0
# p = 0
#
# for c in range(0, 4):
#     dado.append(str(input('Digite o nome: ')))
#     dado.append(int(input('Digite o peso: ')))
#     if len(info) == 0:
#         g = p = dado[1]
#     else:
#         if dado[1] > g:
#             g = dado[1]
#         if dado[1] < p:
#             p = dado[1]
#     info.append(dado[:])
#     dado.clear()
# print(f'Foram cadastradas {len(info)} pessoas.')
# print(f'Com {g}kg As pessoas com maior peso são:', end=' ')
# for j in info:
#     if j[1] == g:
#         print(f'{j[0]}', end=' ')
# print()
# print(f'Com {p}kg As pessoas com menor peso são:', end=' ')
# for j in info:
#     if j[1] == p:
#         print(f'{j[0]}', end=' ')

# Desafio 85
# info = []
# listap = []
# listai = []
# for c in range(0, 7):
#     r = int(input('Digite um numero: '))
#     if r % 2 == 0:
#         listap.append(r)
#     else:
#         listai.append(r)
# info.append(listap[:])
# info.append(listai[:])
# listap.clear()
# listai.clear()
# print(f'Lista de numeros pares {info[0]}')
# print(f'Lista de numeros impares {info[1]}')

# Desafio 86
# matriz = [[0, 0, 0],
#           [0, 0, 0],
#           [0, 0, 0]]
# for l in range(0, 3):
#     for c in range(0, 3):
#         matriz[l][c] = int(input(f'Digite um valor: '))
# print(matriz[0])
# print(matriz[1])
# print(matriz[2])

# Desafio 87
# matriz = [[0, 0, 0],
#           [0, 0, 0],
#           [0, 0, 0]]
# for l in range(0, 3):
#     for c in range(0, 3):
#         matriz[l][c] = int(input(f'Digite um valor: '))
# print(matriz[0])
# print(matriz[1])
# print(matriz[2])
# sum = 0
# for n in matriz[0]:
#     if n % 2 == 0:
#         sum = sum + n
# for n in matriz[1]:
#     if n % 2 == 0:
#         sum = sum + n
# for n in matriz[2]:
#     if n % 2 == 0:
#         sum = sum + n
# print(f'A soma dos valores pares é {sum}')
# sum3c = matriz[0][2] + matriz[1][2] + matriz[2][2]
# print(f'A soma dos valores da 3º coluna é {sum3c}')
# print(f'O maior valor da segunda linha é {max(matriz[1])}')

# Desafio 88
# from random import randint
# from time import sleep
# listac = []
# dados = []
# jogos = int(input('Quantos jogos quer gerar: '))
# for n in range(0, jogos):
#     cont = 0
#     while True:
#         sort = randint(1, 60)
#         if sort not in dados:
#             dados.append(sort)
#             cont = cont + 1
#         if cont >= 6:
#             break
#     listac.append(dados[:])
#     dados.clear()
# for l in range(0, jogos):
#     listac[l].sort()
#     print(f'Jogo {l} >>> {listac[l]}')
#     sleep(1)

# Desafio 89
# listac = []
# while True:
#     dados = str(input('Digite o nome do aluno: '))
#     dados1 = (float(input('Digite a primeira nota: ')))
#     dados2 = (float(input('Digite a segunda nota: ')))
#     media = (dados1 + dados2) / 2
#     listac.append([dados, [dados1, dados2], media])
#     cond = str(input('Quer continuar S/N: ')).lower()
#     while cond not in 'sn':
#         cond = str(input('Escolha S ou N: ')).lower()
#     if cond == 'n':
#             break
# print(listac)
# print(f'{"Nº":<4}{"NOME":<10}{"MEDIA":>8}')
# print('-'*26)
# for i, a in enumerate(listac):
#     print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
# while True:
#     print('-'*30)
#     opc = int(input('Mostrar nota do aluno Nº  (Para finalizar digite 999)'))
#     if opc == 999:
#         break
#     if opc <= len(listac) -1:
#         print(f'Notas de {listac[opc][0]} são {listac[opc][1]}')

print('teste')



