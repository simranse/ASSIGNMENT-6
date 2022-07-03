#Program 2

def Palindrome(string):
    reverse=string[::-1]
    if string==reverse:
        print(string,"is a Palindrome")
    else:
        print(string,"is not a Palindrome")
s=input("Enter any string: ")
Palindrome(s)
    
