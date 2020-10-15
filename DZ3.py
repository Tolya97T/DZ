# Вариант 10
import random
n = int(input("Введиие размер списка:\n"))
A=[]
k=0
for i in range(n):
    a=random.randint(0,99)
    A.append(a)
print(A)
print("В списке "+ str(len(A)) + " значений")
for i in range(n):
    while k < n-3:
        A.pop(i)
        k=k+1
print("Сумма последних трёх цифр: "+str(sum(A)))
l=len(A)
sr=sum(A)/l
print("Среднее арифметическое последний 3-х значений: "+ str(sr))