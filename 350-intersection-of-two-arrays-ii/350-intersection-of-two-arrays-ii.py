class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ht={}
        hm=[]
        for i in nums1:
            if i in ht:
                ht[i]+=1
            else:
                ht[i]=1
        for i in nums2:
            if i in ht and ht[i]!=0:
                hm.append(i)
                ht[i]-=1
        return hm
        