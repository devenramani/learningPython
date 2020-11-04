# Write a function that has a nested list as an argument and calculates the averages of the j th elements in each sub-list. 
# Beware: the length of the list of averages should be as long as  the longest sub-list! 
# For example [[1,2,3],[4,5],[6,7,8,9],[10]] should return[5.25, 4.67, 5.5,  9. 0]  
# (calculated as follows[(1+4+6+10)/4,(2+5+7)/3,(3+8)/2,9/1]).

def longest_nestedlist_length(nestedList):
    maxListLen = 0
    for item in nestedList:
        if(len(item) > maxListLen):
            maxListLen = len(item)

    return maxListLen   

def averageOfList(averageList):
    x = 0
    for item in averageList:
        x += item   
    return x      

def average_nested_list(nestedList):
    
    longestnestedlistlength = longest_nestedlist_length(nestedList)
    average_list = []
    i = 0
    while i < longestnestedlistlength:
        temp = []
        for itemList in nestedList:
            try:
                t = itemList[i]
                temp.append(t)
            except IndexError:
                pass   
        avg = averageOfList(temp)     
        average_list.append(avg/len(temp)) 
        i += 1        
    
    return average_list                

nestedList = [[1,2,3],[4,5],[6,7,8,9],[10]]

average_list = average_nested_list(nestedList)        
print(average_list)