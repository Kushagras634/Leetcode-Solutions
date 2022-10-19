class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        ht={}
        for word in words:
            if word not in ht:
                ht[word]=0
            ht[word]+=1
        li=[]
        heapq.heapify(li)
        for i in ht:
            heapq.heappush(li,[-1*ht[i],i])
        res=[]
        for i in range(k):
            res.append(heapq.heappop(li)[1])
        return res
        