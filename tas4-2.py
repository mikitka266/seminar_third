#Напишите программу, которая будет преобразовывать десятичное число в двоичное.
number = int(input('Введите число в десятичной системе: ')) 
balance = ''
while number > 0:
    balance = str(number % 2) + balance
    number = number // 2
print(balance)