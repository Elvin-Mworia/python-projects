class Solution:
     def palindrome(self,s:list[str])->str:
          
          for w in s:
               l,r=0,len(w)-1 #uses two pointers
               while w[l]==w[r]:
                    if l>=r:
                         return w
                    l+=1
                    r-=1
            # if w==w[::-1]: #alternative method
            #     return w
          return ""
     
problem=Solution()
print(problem.palindrome(["abc","racecar"]))
