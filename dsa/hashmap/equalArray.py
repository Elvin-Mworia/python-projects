from collections import defaultdict
class Solution:
    def ArrayEqual(self,target:list[int],input:list[int]):

        count1,count2=defaultdict(int),defaultdict(int)

        for n1,n2 in zip(target,input):
            count1[n1]=+1
            count2[n2]=+1

        if len(count1) != len(count2):
            return False
        
        for n in count1:
            print(count1[n],count2[n])
            if count1[n]!= count2[n]:
                return False

        return True
    
problem=Solution()

print(problem.ArrayEqual([1,2,3,4],[1,3,4,2]))