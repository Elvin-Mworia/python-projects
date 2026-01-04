class Solution:
    def longestpalindrome(self,s:str)->str:
        res=''
        reslen=0
        for i in range(len(s)):
            #odd length palindrome
            l,r=i,i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1)>reslen:#updating the reslen if we encouner a longer palindrome
                    res=s[l:r+1]
                    reslen=(r-l+1)
                l-=1
                r+=1
            
            #even length palindrome
            l,r=i,i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if(r-l+1)>reslen:
                    res=s[l:r+1]
                    reslen=(r-l+1)
                l-=1
                r+=1

            

        return res
    
problem=Solution()
print(problem.longestpalindrome('babad'))
