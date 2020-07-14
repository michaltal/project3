d=int(input("enter day: "))
m=int(input("enter month: "))
y=int(input("enter year: "))

if 1<=d<=31:
    if 1<=m<=12:
        if 1950<=y<=2020:
            print("%d/%d%d/%d%d"%(d,m//10,m%10,y//10%10,y%10))
        else:
            print("invalid year")
    else:
        print("invalid month")
else:
    print("invalid day")