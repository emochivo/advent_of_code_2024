'''
Advent of Code 2024
Date: 12/1/2024
Written by: Chi Vo
'''

# Create two empty lists to store location IDs.
list1, list2 = [], []

# Read the input file and split it into small elements: each element will have two numbers, one from list 1 and another from list 2.
file = open("input.txt")
content = file.read()
content = content.split("\n")

# Put the numbers into two lists
for i in range(len(content)):
    if content[i] != '':
        temp = content[i].split("   ")
        list1.append(int(temp[0]))
        list2.append(int(temp[1]))

# Sort the list in the ascending order
list1.sort()
list2.sort()

# Calculate the distance and similarity score
distance = 0
similarity_score = 0
for j in range(len(list1)):
    distance += (abs(list1[j]-list2[j]))
    similarity_score += list2.count(list1[j]) * list1[j]

# Print outputs
print("Distance: ", distance)
print("Similarity score: ", similarity_score)