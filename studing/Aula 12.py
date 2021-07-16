# Desafio 36
# house = int(input("Digite o valor da casa: R$"))
# income = int(input("Qual seu salário: "))
# y = int(input("Em quantos anos quer pagar: "))
# y = y * 12
# if (house / y) <= (income * 0.3):
#     print("Seu emprestimo de R${} foi aprovado! Serão {} parcelas de R$ {:.2f}!" .format(house, y, house / y))
# else:
#     print("O emprestimo não foi aprovado.")

# Desafio 37
# n1 = int(input("Type a number: "))
# option = int(input("Type an option: 1- binary, 2- octal, 3- hexadecimal. "))
# if option == 1:
#     print("The binary is:{}" .format(bin(n1)[2:]))
# elif option == 2:
#     print("The octal is: {}" .format(oct(n1)[2:]))
# elif option == 3:
#     print("The hexadecimal is: {}" .format(hex(n1)[2:]))
# else:
#     print("Wrong option!")

# Desafio 38
# n1 = int(input("Type number 1: "))
# n2 = int(input("Type number 2: "))
# if n1 > n2:
#     print("The number 1: {} is greater then number 2: {}." .format(n1, n2))
# elif n2 > n1:
#     print("The number 2: {} is greater then number 1: {}." .format(n2, n1))
# elif n1 == n2:
#     print("Numbers {} and {} are iqual." .format(n1, n2))

# Desafio 39
# y = int(input("Type the year you were born: "))
# y = 2021 - y
# print("You have {} years old" .format(y))
# if y < 18:
#     print("Voce tem {}, ainda não esta na hora de se alistar!" .format(y))
# elif y == 18:
#     print("Voce tem {}, tem que se alistar agora!" .format(y))
# elif y > 18:
#     print("Voce tem {}, já passou do tempo de se alistar" .format(y))

# Desafio 40
# n1 = float(input("Digite a primeira nota: "))
# n2 = float(input("Digite a segunda nota: "))
# if (n1 + n2) / 2 < 5:
#     print("Sua media é {}, voce foi reprovado" .format((n1 + n2) / 2))
# elif (n1 + n2) / 2 >= 5 and (n1 + n2) / 2 <= 6.9:
#     print("Sua media é {}, voce esta de recuperacao" .format((n1 + n2) / 2))
# elif (n1 + n2) / 2 > 7:
#     print("Sua media é {}, voce foi aprovado" .format((n1 + n2) / 2))

# Desafio 41
# y = int(input("Type the year you were born: "))
# y = 2021 - y
# if y <= 9:
#     print("Com {} anos, voce esta na categoria mirim" .format(y))
# elif y <= 14 and y > 9:
#     print("Com {} anos, voce esta na categoria infantil".format(y))
# elif y <= 19 and y> 14 :
#     print("Com {} anos, voce esta na categoria junior".format(y))
# elif y <= 20 and y > 19:
#     print("Com {} anos, voce esta na categoria senior".format(y))
# elif y > 20:
#     print("Com {} anos, voce esta na categoria master".format(y))

# Desafio 42
# l1 = float(input("Type a mesure 1 in cm: "))
# l2 = float(input("Type a mesure 2 in cm: "))
# l3 = float(input("Type a mesure 3 in cm: "))
# if l2 + l3 > l1 > l2 - l3 and l1 + l3 > l2 > l1 - l3 and l2 + l1 > l3 > l2 - l1:
#     print("É possivel formar o triangulo")
#     if l1 == l2 == l3:
#         print("Este é um triangulo Equilatero")
#     elif l1 == l2 or l1 == l3 or l2 == l3:
#         print("Este é um triangulo Isoceles")
#     elif l1 != l2 != l3 and l1 != l3:
#         print("Este é um triangulo Escaleno")
# else:
#     print("Não é possivel formar o triangulo")

# Desafio 43
# w = float(input("Type your weight in Kilos: "))
# h = float(input("Type your hight in meters: "))
# imc = w / (h * h)
# if imc <= 18.5:
#     print("Seu IMC é {}, abaixo do peso" .format(imc))
# elif imc >= 18.5 and imc <= 25:
#     print("Seu IMC é {}, peso ideal".format(imc))
# elif imc > 25 and imc <= 30:
#     print("Seu IMC é {}, sobrepeso".format(imc))
# elif imc > 30 and imc <=  40:
#     print("Seu IMC é {}, obesidade".format(imc))
# else:
#     print("Seu IMC é {}, obesidade morbida".format(imc))

# Desafio 44
# p = float(input("Type the product price: "))
# print("""1- cash:"
# 2- card:
# 3- card 2x:
# 4- card 3x or more:""")
# pay_method = int(input("Pay method: "))
# if pay_method == 1:
#     print("You have 10% off, it will be {:.2f}" .format(p - (p * 0.1)))
# elif pay_method == 2:
#     print("You have 5% off, it will be {:.2f}".format(p - (p * 0.05)))
# elif pay_method == 3:
#     print("It will be {:.2f}".format(p))
# elif pay_method == 4:
#     print("You have 20% increase rate, it will be {:.2f}".format((p * 0.2) + p))

# Desafio 45
# from random import randint
# from time import sleep
# print("""Escolha sua jogada:
# 0- Pedra
# 1- Papel
# 2- Tesoura""")
# p1 = int(input("Sua jogada: "))
# opcoes = ("Pedra", "Papel", "Tesoura")
# pc = randint(0, 2)
# print("Jogada do PC {}" .format(opcoes[pc]))
# print("Jogada do P1 {}" .format(opcoes[p1]))
# print("-=" * 10)
# print("JO")
# sleep(0.8)
# print("KEN")
# sleep(0.8)
# print("PO!!!")
# print("-=" * 10)
# sleep(1)
# if p1 == 0:
#     if pc == 0:
#         print("Empate")
#     elif pc == 1:
#         print("PC Ganhou")
#     else:
#         print("P1 Ganhou")
# elif p1 == 1:
#     if pc == 0:
#         print("P1 Ganhou")
#     elif pc == 1:
#         print("Empate")
#     else:
#         print("Pc Ganhou")
# elif p1 == 2:
#     if pc == 0:
#         print("Pc Ganhou")
#     elif pc == 1:
#         print("P1 Ganhou")
#     else:
#         print("Empate")
# else:
#     print("Jogada invalida")



