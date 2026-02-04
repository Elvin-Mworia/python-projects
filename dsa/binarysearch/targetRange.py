class Solution:
    def findtargetrange(self,nums:list[int],target:int)->list[int]:
        left=self.binarySearch(nums,target,True)
        right=self.binarySearch(nums,target,False)
        return[left,right]

    def binarySearch(self,nums,target,leftBias)->int:
        l,r=0,len(nums)-1
        i=-1
        while l<=r:
            mid=(l+r)//2
            
            if nums[mid]<target:
                l=mid+1
            elif nums[mid]>target:
                r=mid-1
            else:
                i=mid
                if leftBias:
                    r=mid-1
                else:
                    l=mid+1
        return i



problem=Solution()
print(problem.findtargetrange([1,1,4,4,5,5,6,6,6,6,7,7],6))