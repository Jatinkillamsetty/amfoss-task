n=int(input())
ni=list(map(int,input().split()))
nj=set(ni)
for i in nj:
    if ni.count(i)==1:
        print(i)