a=2
b=4
c=a+b
b=c%a
a=a+b
b=a+c
for i in range (1,2):
    b=b-i
    print(b)