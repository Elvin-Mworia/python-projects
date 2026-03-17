from collections import Counter
class Solution:

    def commonletters(self,words:list[str])->list[str]:
        ref_word=Counter(words[0])
        res=[]
        #print(words[1::])
        for  w in words[1::]:
            curr_word=Counter(w)
            for c in w:
                #print(ref_word[c],curr_word[c])
                ref_word[c]=min(ref_word[c],curr_word[c])
        #print(ref_word)

        for c in ref_word:
            for i in range(ref_word[c]):
                res.append(c)
        #print(ref_word)
        return res
    
problem=Solution()

print(problem.commonletters(["at","ba","r"]))