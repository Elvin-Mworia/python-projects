class Solution:
    def arraydiff(self,nums1:list[int],nums2:list[int])->list[list[int]]:
            numset1,numset2= set(nums1),set(nums2)
            res1,res2=set(),set()

            for n in nums1:
                  if n not in numset2:
                        res1.add(n)

            for n in nums2:
                  if n not in numset1:
                        res2.add(n)

            return [list(res1),list(res2)]
    


problem=Solution()

print(problem.arraydiff([1,2,4,5],[1,4,7,8]))