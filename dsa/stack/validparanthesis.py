class Solution:
    def isValidParenthis(self,input:str)->bool:
        stack=[]
        closingBrace={")":"(","}":"{","]":"["}

        for s in input:
            if s in closingBrace:
                 '''matching if the outer/closing brace encountered has an associated opening brace on top of the stack '''
                 if stack and stack[-1]==closingBrace[s]:    
                    stack.pop()
                 else:
                     return False
            else:
                stack.append(s)     
            
        return True if not stack else False #returnig True if and only if the stack is empty otherwise False
 
problem=Solution()

print(problem.isValidParenthis("[]{}()"))