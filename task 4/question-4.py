a=input()
b=[]
for i in a:
    if i.isdigit():
        b.append(i)

f={0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
for i in range(10):
    for k in b:
        if  str(i)==k:
            f[i]=f[i]+1
    
for i in f:
    print(f[i],end=" ")