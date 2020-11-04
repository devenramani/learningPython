mylist = [1,0,-5,0,4,-2,0,-4]

#1 Write a list comprehension that replaces all elements in the list of numbers with their absolute value.[1,-1,3,-5]→[1,1,3,5]

absoluteElements = [abs(x) for x in mylist]
print(absoluteElements)

#2 Write a list comprehension that only contains the positive numbers occurring in a given list. [1,-1,3,-5]→[1,3]

positiveElements = [x for x in mylist if x >= 0]
print(positiveElements)

#3 Write a list comprehension that replaces all zeros in a list with -1.  [1,0,3,0]→[1,-1,3,-1]

replaceZeros = [-1 if x == 0 else x for x in mylist]
print(replaceZeros)

#4  Write a list comprehension that converts all lowercase characters in a list to uppercase (other char-acters like space, coma,...  should remain unchanged).  
# [“a”, “b”, “C”]→[“A”, “B”, “C”]
letters = ['a','b','c']
uppercase = [x.upper() for x in letters]
print(uppercase)

#5  Use a list comprehension to make a list of the first 10 powers of 2 starting from 1.

pow()