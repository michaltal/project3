sentence = input("enter sentence: ")
print(sentence)

# length
print(len(sentence))

# letters in location 3 to 6
print(sentence[3:7])

# convert to list and print first word 3 times
list1 = sentence.split(' ')
print(list1)
print(list1[0] * 3)

# print the sentence with first capital letter in every word

for word in list1:
    print(word.capitalize())
