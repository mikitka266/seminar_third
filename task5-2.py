#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.(Доп)
fib1 = fib2 =1
n=int(input("Введите число: ")) 
list_3= [-1, 1, 0, 1, 1]
list_1 =[]
list_2 =[]
for i in range(2, n):
    fib1, fib2 = fib2, fib1 + fib2
    list_1.insert(i, fib2)
    if i%2==0:
        list_2.insert(i,fib2)
    if i%2!=0:
        list_2.insert(i,-fib2)
list_2.reverse()
list_2.extend(list_3)
list_2.extend(list_1)   
print(list_2)


 