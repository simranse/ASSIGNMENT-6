#Program 9:

class parentheses:
   def is_valid(self, str1):
        stack, pchar = [], {"(": ")", "{": "}", "[": "]"}
        for parenthese in str1:
            if parenthese in pchar:
                stack.append(parenthese)
            elif len(stack) == 0 or pchar[stack.pop()] != parenthese:
                return False
        return len(stack) == 0
print(parentheses().is_valid("(){}[]"))
print(parentheses().is_valid("()[{)}"))
print(parentheses().is_valid("()"))
print(parentheses().is_valid("{{{"))
