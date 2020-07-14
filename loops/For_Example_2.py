sum=0
count=0

for i in range(5):
    price = int(input("enter price: "))

    sum+=price
    count+=1
    if sum>=1000:
        print("too expensive!!! I don't want this product")
        break
else:
    print("I bought all products, we are not over 1000")
print(sum)
print(sum/count)