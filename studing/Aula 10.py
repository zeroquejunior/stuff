# Desafio 28
# from random import randint
# rn = randint(0, 5) # Estava tentando com random.sample, porem ele puxa de uma lista e o if não estava fazendo a comparação
# print(rn)
# guess = int(input("Guess the number from 0 to 5:"))
# if guess == rn:
#     print("Good guess, you are right!")
# else:
#     print("Not this time. The number was {}" .format(rn))

# Desafio 29
# from random import randint
# car_speed = randint(0, 200)
# print("Speed trap {} Km/h" .format(car_speed))
# if car_speed > 80:
#     fine = (car_speed-80) * 7
#     print("You are exceeding the speed limit of 80 Km/h! The fine for that is R$ {:.2f}!" .format(fine))

# Desafio 30
# number = int(input("Type a number: "))
# if (number % 2) == 0:
#     print("The number {} is even!" .format(number))
# else:
#     print("The number {} is odd!" .format(number))

# Desafio 31
# km = int(input("Type how many km your destiny is: "))
# if km <= 200:
#     ticket1 = float(km * 0.50)
#     print("It will be R$ {} for the trip!" .format(ticket1))
# else:
#     ticket2 = float(km * 0.45)
#     print("It will be R$ {} for the trip!".format(ticket2))

# Desafio 32
# year = int(input("Type a year: "))
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print("{} é um ano bissexto!".format(year))
# else:
#     print("{} não é um ano bissexto" .format(year))

# Desafio 33
# n1 = int(input("Type number 1: "))
# n2 = int(input("Type number 2: "))
# n3 = int(input("Type number 3: "))
# if n1 > n2 and n1 > n3:
#     maior = n1
# if n2 > n1 and n2 > n3:
#     maior = n2
# if n3 > n1 and n3 > n2:
#     maior = n3
# print("{} é o maior numero!" .format(maior))
# if n1 < n2 and n1 < n3:
#     menor = n1
# if n2 < n1 and n2 < n3:
#     menor = n2
# if n3 < n1 and n3 < n2:
#     menor = n3
# print("{} é o menor numero!" .format(menor))

# Desafio 34
# your_income = int(input("Type your income:R$ "))
# if your_income > 1250:
#     your_income = your_income + (your_income * 0.10)
# if your_income < 1250:
#     your_income = your_income + (your_income* 0.15)
# print("Your income now is R${:.2f} " .format(your_income))

# Desafio 35
# l1 = float(input("Type a mesure 1 in cm: "))
# l2 = float(input("Type a mesure 2 in cm: "))
# l3 = float(input("Type a mesure 3 in cm: "))
# if l2 + l3 > l1 > l2 - l3 and l1 + l3 > l2 > l1 - l3 and l2 + l1 > l3 > l2 - l1:
#     print("É possivel formar o triangulo")
# else:
#     print("Não é possivel formar o triangulo")

