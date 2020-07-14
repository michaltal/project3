str1=input("enter word: ")

for a in str1:
    print(a)

print("==================")

for i in range(len(str1)):
    print(i)
    print(str1[i])

print("==================")
print(str1[len(str1)-1])
print("==================")

ch = input("enter character: ")

print(not ch in str1)

if not ch in str1:
    print("not found")
else:
    print("found")

a=5
b=6
c="abc"

print("a={0} b={1} a+b={0}+{1} c={2}".format(a,b,c))

print(f'a={a} b={b} a+b={a+b} c={c}')

