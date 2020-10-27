def trib(n):
    a, b,c, counter = 0, 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b, c= b ,b+c, b+a
        counter += 1
f = trib(35)
for x in f:
    print(x, " ", end="")