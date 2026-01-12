#modified binary search

class Solution:

    def peakElement(self,input:list[int])->int:
        l,r=0,len(input)-1

        while l<=r:

            m=l+((r-l)//2)
            print(m)
            if m>0 and input[m]<input[m-1]:
                r=m-1
            elif m < len(input) and input[m]<input[m+1]:
                l=m+1
            else:
                return m

problem=Solution()

print(problem.peakElement([1,2,3,1]))

