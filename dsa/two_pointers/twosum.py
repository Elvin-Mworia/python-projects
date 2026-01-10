class Solution:
    def twoSum(self,input:list[int],target:int)->list[int]:
        l,r=0,len(input)-1

        while l<r:
            if input[l]+input[r]>target:
                r-=1
            elif input[l]+input[r]<target:
                l+=1
            else:
                return [l+1,r+1]



problem=Solution()

print(problem.twoSum([2,7,11,15],9))#the input array should be sorted and the indexes are 1 based