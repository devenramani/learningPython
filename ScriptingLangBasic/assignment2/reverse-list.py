orignalList = [1,2,3,4,5]

def reverse(lst):
    i = 0            # first item
    j = len(lst)-1   # last item
    while i<j:
        lst[i],lst[j] = lst[j],lst[i]
        i += 1
        j -= 1
    return lst

reversedList = reverse(orignalList)   
print(reversedList)

#reversing without iterations
#print(orignalList[::-1])
