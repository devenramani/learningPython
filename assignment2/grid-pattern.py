def create_corners(x,y):
    s = '#' + (('-'*x) + '#')*y 
    print(s)
    
def create_central(x,y):
    s = '|' + ((' '*x) + '|')*y 
    print(s)

def create_grid(w,h,s):

    create_corners(w,s)  
    x = 0
    while x < s:
        i = 0
        while i < h:
            create_central(w,s)
            i+= 1
        
        create_corners(w,s)
        x+=1

#parameters -> create_grid(width,height,squares)
create_grid(5,5,5)