class Solution:
    def findMin(self,nums:list[int])->int:
        res=min(nums[0],nums[-1])
        l,r=0,len(nums)-1

        while l<=r:
            if nums[l]< nums[r]:
                res=min(res,nums[l])
                break
            mid=(l+r)//2
            print(mid)
            print(nums[l],nums[r])
            res=min(res,nums[mid])
            if nums[mid]>=nums[l]:
                l=mid+1
            else:
                r=mid-1
        return res
problem=Solution()

print(problem.findMin([3,4,5,6,7,8,1,2]))