class Solution:
    def reverseString(self,s:str)->str:
        sen=list(s)
        print(sen)
        l=0
        for r in range(len(sen)):
            if sen[r]==" " or r==len(s)-1:
                temp_l,temp_r=l,r-1
                if r ==len(sen)-1:
                    temp_r=r
                while temp_l<temp_r:#reversing word
                    sen[temp_l],sen[temp_r]=sen[temp_r],sen[temp_l]
                    temp_l+=1
                    temp_r-=1
                l=r+1
        return "".join(sen)
    
problem=Solution()
print(problem.reverseString("Today is Sunday"))