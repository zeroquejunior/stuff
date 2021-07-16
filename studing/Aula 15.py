# Desafio 66
# i = 0
# list = []
# while True:
#     i = int(input('Digite um numero (999 para parar):'))
#     if i == 999:
#         break
#     list.append(i)
# print(f'Foram digitados {len(list)} numeros')
# print(f'O resultado da soma entre eles é {sum(list)}')

# Desafio 67
# while True:
#     n = int(input('Digite um numero para ver sua tabuada: '))
#     if n < 0:
#         break
#     for c in range(1, 11):
#         t = n * c
#         print(f'{n} x {c} = {t}')
# print('Programa finalizado')

# Desafio 68
# from random import randint
# w = 0
# print('VAMOS JOGAR PAR ou IMPAR!')
# while True:
#     pc = randint(0, 5)
#     p1 = int(input('Digite seu numero de 1 a 5:'))
#     if p1 > 5:
#         break
#     c = str(input('Quer PAR ou IMPAR?: '))
#     r = pc + p1
#     if c == 'par' and r % 2 == 0:
#         print(f'A soma é {r} = PAR. Vc GANHOU!')
#         w = w + 1
#     else:
#         print(f'A soma é {r} = IMPAR. Vc PERDEU')
#         break
# print(f'Vc ganhou {w} vezes, parabens!')
# print('Jogo finalizado.')

# Desafio 69
# a = 0
# b = 0
# c = 0
# while True:
#     idade = int(input('Digite a idade:'))
#     sexo = ' '
#     while sexo not in 'MF':
#         sexo = str(input('Digite o sexo M/F: ')).upper()[0]
#     if idade > 18:
#         a = a + 1
#     if sexo == 'M':
#         b = b + 1
#     if sexo == 'F' and idade < 20:
#         c = c + 1
#     con = ' '
#     while con not in 'SN':
#         con = str(input('Cadastrar novo? S ou N:')).upper()
#     if con == 'N':
#         break
# print(f'Temos {a} pessoas com mais de 18 anos.')
# print(f'Foram cadastrados {b} homens.')
# print(f'Temos {c} mulheres com menos de 20 anos.')

# Desafio 70
# compra = []
# cpreco = 0
# barato = ''
# contador = 0
# menor_preco = 0
# while True:
#     produto = str(input('Digite o nome do produto: ')).lower()
#     preco = float(input('Digite o valor do produto: '))
#     contador = contador + 1
#     compra.append(preco)
#     continuar = str(input('Deseja continuar com a compra [S/N]: ')).upper()
#     if preco > 1000:
#         cpreco = cpreco + 1
#     if contador == 1 or preco < menor_preco:
#         menor_preco = preco
#         barato = produto
#     while continuar not in 'SN':
#         continuar = str(input('Deseja continuar com a compra [S/N]: ')).upper()
#     if continuar == 'N':
#         break
# print(f'>>>O total gasto na compra foi R${sum(compra)}<<<')
# print(f'>>>{cpreco} produtos cutam mais de R$ 1000,00<<<')
# print(f'>>>O produto mais barato é o {barato}<<<')

# Desafio 71
c = 50
contc = 0
saque = int(input('Digite o valor a ser sacado R$: '))
total = saque
while True:
    if total >= c:
        total = total - c
        contc = contc + 1
    else:
        if contc > 0:
            print('=' *30)
            print(f'Total de {contc} cedulas de R$ {c}')
        if c == 50:
            c = 20
        elif c == 20:
            c = 10
        elif c == 10:
            c = 1
        contc = 0
        if total == 0:
            break
print('=' * 30)





