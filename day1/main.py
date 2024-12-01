'''
Advent of Code 2024
Date: 12/1/2024
Written by: Chi Vo
'''

list1, list2 = [], []

file = open("input.txt")
content = file.read()

content = content.split("\n")

for i in range(len(content)):
    if content[i] != '':
        temp = content[i].split("   ")
        list1.append(int(temp[0]))
        list2.append(int(temp[1]))

list1.sort()
list2.sort()

distance = 0
similarity_score = 0
for j in range(len(list1)):
    distance += (abs(list1[j]-list2[j]))
    similarity_score += list2.count(list1[j]) * list1[j]

print("Distance: ", distance)
print("Similarity score: ", similarity_score)