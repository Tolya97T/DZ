a= int(input("введите сторону а:\n "))
b= int(input("введите сторону b:\n "))
n = 0
print("Прямоугольник", str(a),"x", str(b))
def pryam(a,b,n):
    if n >= 1:
        print("размер квадрата: ", max(a,b), "x", max(a,b))
    if a == b:
        print("размер квадрата: ", max(a, b), "x", max(a, b))
        return n+1
    if a > b:
        return pryam(a-b,b,n+1)
    if a<b:
        return pryam(a,b-a,n+1)
print("количество квадратов: ",str(pryam(a,b,n)))