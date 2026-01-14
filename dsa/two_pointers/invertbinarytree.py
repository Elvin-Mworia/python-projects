class Solution:

    def invertBinaryTree(self,nums:list[int])->list[int]:
        l,r=0,len(nums)-1

        while l<r:
            nums[r],nums[l]=nums[l],nums[r]
            r-=1
            l+=1
        
        return nums
    
problem=Solution()
print(problem.invertBinaryTree([1,2,3,4,6,7,9]))