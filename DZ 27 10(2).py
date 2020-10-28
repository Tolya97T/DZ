f1 = open('f1.txt')
f2 = open('f2.txt','w')
a=-1
for i in f1:
    if a % 2 == 0:
        f2.write(i)
    a+=1


f1.close()
f2.close()