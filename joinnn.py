n=int(input("no bolo ?? - "))
a=list(range(1,n+1))
print(a)
#converting list elemnt to string
b=[]
for x in a:
    b.append(str(x))
print(b)
#now "".join(str)
c="".join(b)
print(c)