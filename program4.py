#Program 4:

import string
def ispangram(str):
   alphabet = "abcdefghijklmnopqrstuvwxyz"
   for char in alphabet:
      if char not in str.lower():
         return False
   return True

string =input("Enter any string: ")
if(ispangram(string) == True):
   print("It is a pangram!")
else:
   print("It is not a pangram!")

