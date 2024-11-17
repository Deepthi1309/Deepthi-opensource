a,b,c = map(int,input().split())
if c%b==0 and a*b>=c:
    print("YES")
else:
    print("NO")
