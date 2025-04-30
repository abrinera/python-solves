#Maximum of Three Numbers

x,y,z= map(int,input().strip().split())
if x>y:
    if x>z:
        print(x)
    else:
        print(z)
else:
    if y>z:
        print(y)
    else:
        print(z)                