import heapq
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        li=[]
        for i in range(len(speed)):
            li.append([efficiency[i],speed[i]])
        li.sort(key=lambda x: int(x[0]))
        li=li[::-1]
        res,speed=0,0
        minHeap=[]
        for eff, spd in li:
            if len(minHeap)==k:
                speed-=heapq.heappop(minHeap)
            speed+=spd
            heapq.heappush(minHeap,spd)
            res=max(res,eff*speed)
        return res%(10**9+7)
        
        