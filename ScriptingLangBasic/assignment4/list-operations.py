"""
The following function should check if an element appears in a list and returns the (first)
index of that element.
"""
def find(list, element):
    for i in range(len(list)):
        if (list[i] == element):
            return i
    return 'Element not found in list'


list = [1, 4, 7, 6, 2, 12, 8, 9]
print(find(list, 7))



"""
This function is supposed to reverse the elements of a list
"""
def reverseList(list):
    reversed = []
    for i in range(len(list)-1, -1, -1):
        reversed.append(list[i])
    return reversed


list = [0, 1, 2, 3, 4, 5]
print(reverseList(list))



"""
This function is supposed to check whether a list is sorted in increasing order. The result
of this function should be a Boolean value
"""
def isSorted(mylist): 
    for i in range(len(mylist)):
        first_element = mylist[i]
        if i == len(mylist)-1:
            second_element = first_element
        else:
            second_element = mylist[i+1]

        if(first_element <= second_element):
            indicator = True
        else:
            indicator = False
        return False
    
    if indicator == True:
        return True

print(isSorted([9, 1, 2, 3]))
