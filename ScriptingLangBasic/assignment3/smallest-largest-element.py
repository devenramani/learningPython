#Write a function that returns the smallest and largest element in a list (without using the built-in Python functionsand methods such assort, min and max!).
#Note that the function returns two values!

def smallest_largest_element(elementList):
    
    smallest_element = elementList[0]
    largest_element = elementList[0]

    for item in elementList:
        if(item < smallest_element):
            smallest_element = item

        if(item > largest_element):
            largest_element = item

    return smallest_element,largest_element             

elementList = [24,45,6,23,19,3,80,65,1,57,94,99,3]

smallest,largest = smallest_largest_element(elementList)
print('Smallest Element: {0} Largest Element: {1}'.format(smallest,largest))  