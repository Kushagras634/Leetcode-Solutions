class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        ht={}
        li=[]
        for i in range(len(s)-9):
            if s[i:i+10] in ht:
                ht[s[i:i+10]]+=1
            else:
                ht[s[i:i+10]]=1
        for i in ht:
            if ht[i]>1:
                li.append(i)
        return li
                  