class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        li='abcdefghijklmnopqrstuvwxyz'
        ht={}
        for i in sentence:
            if i not in ht:
                ht[i]=1
            ht[i]+=1
        for i in li:
            if i not in ht:
                return False
        return True