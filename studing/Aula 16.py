# Desafio 72
# contagem = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezeseis' ,'dezesete','dezoito', 'dezenove', 'vinte')
#
# while True:
#     leitor = int(input('Digite um numero entre 0 e 20: '))
#     if 0 <= leitor <= 20:
#         break
#     print('Tente novamente!', end='')
# print(f'O valor digitado é {contagem[leitor]}')

# Desafio 73
# brasileirao = ('palmeiras', 'bragantino', 'atleticomg', 'fortaleza', 'athleticopr', 'bahia', 'fluminense', 'flamengo', 'santos', 'atleticogo', 'ceara', 'corinthians', 'juventude', 'sao paulo', 'internacional', 'ameriacamg', 'sport', 'cuiaba', 'chapecoense', 'gremio')
# print(f'Os 5 primeiros colocados são: {brasileirao[0:5]}')
# print(f'Os 4 ultimos colocados são: {brasileirao[-4:]}')
# print(f'Lista de times em ordem alfabetica: {sorted(brasileirao)}')
# print(f'A chapecoense é o {brasileirao.index("chapecoense")+1} colocado')

# Desafio 74
# from random import randint
# r = (randint(1, 99), randint(1, 99), randint(1, 99), randint(1, 99), randint(1, 99))
# print(r)
# print(f'O menor numero é {min(r)}')
# print(f'O maior numero é {max(r)}')

# Desafio 75
# t = (int(input('Digite um valor: ')), int(input('Digite um valor: ')), int(input('Digite um valor: ')),int(input('Digite um valor: ')))
# print(f'O valor 9 aparece {t.count(9)} vezes.')
# print(f'O valor 3 aparece na posição {t.index(3)} pela primeira vez')
# for c in t:
#     par = c % 2
#     if par == 0:
#         print(f'{c} é par')

# Desafio 76
# estoque = ('Banana', 2, 'Maça', 3, 'Arroz', 15)
# print(estoque[0], end=' = ')
# print(estoque[1])
# print(estoque[2], end=' = ')
# print(estoque[3])
# print(estoque[4], end=' = ')
# print(estoque[5])

# ou
# estoque = ('Banana', 2, 'Maça', 3, 'Arroz', 15)
# print('-' * 30)
# print('LISTAGEM DE PREÇOS')
# print('-' *30)
# for pos in range (0, len(estoque)):
#     if pos % 2 ==0:
#         print(f'{estoque[pos]:.<30}', end='')
#     else:
#         print(f'R${estoque[pos]:>7.2f}')

# Desafio 77
# palavras = ('macaco', 'bola', 'cavalo', 'chiqueiro')
# for voc in palavras:
#     print(f'\nNa palavra {voc.upper()} temos', end='')
#     for letra in voc:
#         if letra.lower() in 'aeiou':
#             print(letra, end=' ')



