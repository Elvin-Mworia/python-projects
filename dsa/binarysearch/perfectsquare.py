class Solution:

    def isPerfectSquare(self,num)->bool:
        
        # for i in range(0,num+1):
        #     if i*i ==num:
        #         return True
        #     elif i*i>num:
        #         return False
            

        l,r=0,num    
        while l<=r:
            mid=(l+r)//2
            if mid*mid<num:
                l=mid+1
            elif mid*mid>num:
                r=mid-1
            else:
                return True
        return False
    
problem=Solution()

print(problem.isPerfectSquare(100))