#Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

list_1 = [1 , 2, 3, 7,8,9,12,15,12,14]
result=0
for i in range(len(list_1)):
    if i//2!=0:
        result+=list_1[i]
print(result)