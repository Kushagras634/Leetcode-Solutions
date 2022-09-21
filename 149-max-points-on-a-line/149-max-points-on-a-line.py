class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points)<=2:
            return len(points)
        l=len(points)
        m=0
        for i in range(l):
            ht={}
            for j in range(i+1,l):
                if points[i][0]==points[j][0]:
                    t=float('inf')
                else:
                    t=(points[j][1]-points[i][1])/(points[j][0]-points[i][0])
                if t in ht:
                    ht[t]+=1
                else:
                    ht[t]=1
                m=max(m,ht[t])
        return m+1
                
        
            
        
        
        