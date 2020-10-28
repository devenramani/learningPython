def print_star(len):
    for x in range(1,len+1):
        s = '*'*x
        print(s)

    for x in reversed(range(len)):
        s = '*'*x
        print(s)  

print_star(10)
        