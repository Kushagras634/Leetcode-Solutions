class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        i=0
        j=len(tokens)-1
        mx=0
        score=0
        
        while i<=j:
            if power>=tokens[i]:
                power-=tokens[i]
                i+=1
                score+=1
                mx=max(mx,score)
            elif score>0:
                score-=1
                power+=tokens[j]
                j-=1
            else:
                break
        return mx
            
        