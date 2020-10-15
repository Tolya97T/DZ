# Вариант 14
K = int(input("Введите возраст от 1 до 9:\n"))
a=" год"
b=" лет"
c=" года"
if K == 1:
    print("мне "+str(K)+ a)
elif K > 1 and K < 5:
    print("мне " + str(K) + c)
elif K >= 5 and K <= 9:
    print("мне " + str(K) + b)
else:
    print("Вам больше 9 лет!")