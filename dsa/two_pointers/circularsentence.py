class Solution:
    def isCircular(self,sen:str)->bool:
        sentence=sen.split(" ")
        print(sentence)

        # for i in range(len(sentence)):
        #     if sentence[i]==" " and sentence[i-1][-1]!=sentence[i+1][0]:
        #         return False
        # if sentence[0][0]!=sentence[-1][-1]:
        #     return False
        for i in range(len(sentence)):
            if sentence[i][0]!=sentence[i-1][-1]:
                return False
        return True
problem=Solution()

print(problem.isCircular("leetcode exercises sound delightful"))