def checkleapyear(x):
    if(x%4 == 0 and x%100 != 0 or x%400 == 0):
        return True
    else:
        return False

year = int(input("Enter Year: "))
flag = checkleapyear(year)

if(flag == True):
    print("{0} is a Leap Year".format(year))
else:
    print("{0} is not a Leap Year".format(year))