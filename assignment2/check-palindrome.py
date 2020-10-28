def check_palindrome(word):
    for i in range(0,len(word)//2):
        if word[i] == word[-1-i]:
            check = True
        else:
            return False
    return check   

print(check_palindrome(input("Enter word to check if Palindrome : ")))