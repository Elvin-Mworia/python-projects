class Solution:

    def stringPartition(self,input:str)->int:
        curSet=set()
        res=1

        for c in input:
            if  c in curSet:
                res+=1
                curSet=set()
            curSet.add(c)
        return res

problem=Solution()
print(problem.stringPartition("abacaba"))

