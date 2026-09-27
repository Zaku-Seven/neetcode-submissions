class Solution:
    def isValid(self, s: str) -> bool:

        stack = []


        for i in s:
            if i in ('(', '[', '{'):
                stack.append(i)

            if i in (')',']','}'):
                if len(stack) !=0:
                    if i == ')' and stack[-1] != '(':
                        return False
                    if i == ']' and stack[-1] != '[':
                        return False
                    if i == '}' and stack[-1] != '{':
                        return False
                
                    stack.pop()
                else:
                    return False

               
            
        
        if len(stack) == 0:
            return True
        
        else:
            return False
        

        
        