#Задайте список из вещественных чисел. 
#Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
list_1 = [1.2 , 2.555, 3.0001, 7.2222,8.14123,9.232344,12.43452343,15.9097544,12.22333,14.333322]
min=1
max=0
temp=0
for i in range(len(list_1)-1):
    temp =i - int(i)
    if(temp<min):
        min=temp
    if(temp>max):
        max=temp
print({max}-{min})