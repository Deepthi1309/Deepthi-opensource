a=int(input())
b=list(map(int,input().split()))
for i in range(0,a):
    print(b[a-i-1],end=" ")
