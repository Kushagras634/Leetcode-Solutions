# from itertools import permutations
# class Solution:
#      def findSubstring(self, s: str, words: List[str]) -> List[int]:
#             wlen=len(words[0])
#             wslen=len(words)*len(words[0])
#             res=[]
#             for pos in range(wlen):
#                 i=pos
#                 d=Counter(words)
#                 for j in range(i,len(s)+1-wlen,wlen):
#                     word=s[j:j+wlen]
#                     d[word]-=1
#                     while d[word]<0:
#                         d[s[i:i+wlen]]+=1
#                         i+=wlen
#                         if i+wslen==j+wlen:
#                             res.append(i-wlen)
#             return res
            
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        wlen = len(words[0])
        wslen = len(words) * len(words[0])
        res = []
        
        for pos in range(wlen):
            i = pos
            d = Counter(words)
            
            for j in range(i, len(s) + 1 - wlen, wlen):
                word = s[j: j + wlen]
                d[word] -= 1
                
                while d[word] < 0:
                    d[s[i: i + wlen]] += 1
                    i += wlen
                if i + wslen == j + wlen:
                    res. append(i)
        
        return res
            
            
            
            
            
    # Complexity:O(n!+n)
    # def findSubstring(self, s: str, words: List[str]) -> List[int]:
    #     li=[]
    #     perm=list(permutations(words))
    #     for i in range(len(perm)):
    #         perm[i]=''.join(perm[i])
    #     temp=len(words)*len(words[0])
    #     for i in range(len(s)-temp+1):
    #         if s[i:i+temp] in perm:
    #             li.append(i)
    #     return li
            
        
        