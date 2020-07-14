# i=1
# while i<=10:
#     print("hello",i)
#     i+=1

# for i in range (10,1,-2):
#     print(i)

sum=0
count=0

for i in range(5):
    price = int(input("enter price: "))

    if sum+price>=1000:
        print("too expensive!!! I don't want this product")
        continue

    sum+=price
    count+=1

print(sum)
print(sum/count)