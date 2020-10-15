# Вариант 2
p = 100
q = 516
x = 1
while p < q:
    p = p+p*0.03
    print(p)
    x= x+1
print("Понадобится "+ str(x) +" дней")