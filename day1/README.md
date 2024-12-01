ADVENT OF CODE DAY 1: Historian Hysteria (Link: https://adventofcode.com/2024/day/1)

There are two main problems:

Part 1: Find the sum of the differences obtained from two numbers having the same order level in two lists of numbers. 
In other words, the smallest number in list 1 will be paired with the smallest number in list 2, the second-smallest number in list 1 will be paired with the second-smallest number in list 2, and so on. Our mission is to find the differences of all numbers in two lists and sum it up!   

Part 2: Find the sum of the similarity score for these two lists. Similarity score will be calculated by multiplying the number of list 1 with the quantity of that number in list 2. 
For example, if number 2 does appear in list 1, and it appears 3 times in list 2, the similarity score for that number will be 2x3=6; if number 2 isn't in list 2, the similarity score will be 2x0=0. The problem counts duplicates: so if number 2 appears 4 times in list 1, we will calculate the similarity score for it 4 times. Find the similarity scores of all numbers in two lists and sum it up! 


My approach for these two problems:
- Read the input file and somehow break the input into smaller chunks so that I can put them into two seperate lists.
- Sort them so that they run from the ascending order.
- Use a for loop to find both the distance total and the similarity score total.  
