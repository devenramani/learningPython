# Write a function that takes a nested list as argument, and returns the length of the longest list. 
# For example: [[1,2,3],[4,5],[6,7,8,9],[10]] -> 4 since the longest list is [6,7,8,9] and its length is 4.

def longest_nestedlist_length(nestedList):
    maxListLen = 0
    for item in nestedList:
        if(len(item) > maxListLen):
            maxListLen = len(item)

    return maxListLen        

nestedList = [[1,2,3],[4,5,4],[6,7,8,9,2,5],[10],[2,8]]

length = longest_nestedlist_length(nestedList)

print("Longest List Length : ", length)