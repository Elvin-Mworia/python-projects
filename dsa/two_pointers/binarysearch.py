class Solution:
    def binarySearch(self,nums:list[int],num:int )->int:
        l,r=0,len(nums)-1
        while l<=r:
            m=l+((r-l)//2)#midpoint calculation if index numbers are arbitrally large
            if nums[m]>num:
                r=m-1
            elif nums[m]<num:
                l=m+1
            else:
                return m


        return -1

problem=Solution()
print(problem.binarySearch([2,7,11,15],11))