class Solution:
    def intersection(self,nums1:list[int],nums2:list[int])->list[int]:
        seen=set(nums1)
        res=[]
        for n in nums2:
            if n in seen:
                res.append(n)
                nums2.remove(n)

        return res
    
problem=Solution()

print(problem.intersection([1,3,4,5],[2,4,6]))