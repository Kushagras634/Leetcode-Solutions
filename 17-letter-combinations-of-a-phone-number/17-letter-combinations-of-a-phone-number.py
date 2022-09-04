class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ht={
            2:"abc",
            3:"def",
            4:"ghi",
            5:"jkl",
            6:"mno",
            7:"pqrs",
            8:"tuv",
            9:"wxyz"       
        }
        li=[]
        def digit(digits,i,s):
            if len(digits)==0:
                return
            if i==len(digits):
                li.append(s)
                return
            if i>len(digits):
                return
            
            for j in ht[int(digits[i])]:
                digit(digits,i+1,s+j)
        digit(digits,0,"")
        return li
            
        