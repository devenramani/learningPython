"""
Create a string variable that is assigned the following sentence:
“Zeven Zottegemse zotten zullen zes zomerse zondagen zwemmen zonder zwembroek.”

a.Count the number of words in that sentence. Hint: strings have the methodsplit()that returns a list with each word of that sentence as an element. len(mylist)returns the length of your list.
b.Replace for every word the first letter by a ‘p’. Hint: the string type has the methodreplace(old,new),  which  replaces  a  substring oldwith another substringsubstring new. Be careful: this method is case sensitive!
"""

s = "zeven zottegemse zotten zullen zes zomerse zondagen zwemmen zonder zwembroek"

sarray = s.split()

for index,s in enumerate(sarray):
     sarray[index]= sarray[index].replace('z','p')

print(sarray)