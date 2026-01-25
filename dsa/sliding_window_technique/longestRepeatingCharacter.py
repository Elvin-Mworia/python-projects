class Solution:
     def longestRepeatingCharacterReplacement(self,s:str,k:int)->int:
          count={}
          l=0
          res=0

          for r in range(len(s)):
               count[s[r]]=1 +count.get(s[r],0)

               while count[s[l]]-max(count.values())>k:
                    count[s[l]]-=1
                    l+=1
               res=max(res,r-l+1)
          print(res)
          return res

problem=Solution()

problem.longestRepeatingCharacterReplacement('ababba',2)
