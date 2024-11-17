p,q,r,s=map(int,input().split())
if p+q>=s or q+r>=s or r+p>=s :
    print("YES")
else:
    print("NO")
