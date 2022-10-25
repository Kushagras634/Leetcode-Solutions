class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        wor1=''.join(word1)
        wor2=''.join(word2)
        if wor1==wor2:
            return True
        return False
        
        