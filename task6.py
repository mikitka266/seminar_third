#Требуется написать программу, производящую согласно утверждению Гольдбаха, разложение заданного чётного числа. Из всех пар простых чисел, сумма которых равна заданному числу, 
#требуется найти пару, содержащую наименьшее простое число.

n=int(input("Введите число: "))
def Goldbah (n):
    k=2
    while k*k<=n and n%k !=0:
        d+=1
    return k*k>n
    
if n==4:
     print(f'число 4 раскладывается на 2,2')
else:
     k=3
     while not Goldbah(k) or not Goldbah(n-k):
         k+=1
     print(f'Число {n} раскладывается на числа {k} и {n-k}')


