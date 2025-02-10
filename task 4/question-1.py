n = int(input())
ni = list(map(int, input().split()))
m = int(input())
mi = list(map(int, input().split()))
l=[]

ns=set(ni)
ms=set(mi)
for i in ns:
    if ni.count(i)!=mi.count(i):
        l.append(i)
l.sort()
for k in l:
    print(k ,end=" ")
print()