class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        li=[]
        def recurse(current):
            if len(current)==n:
                li.append(int(''.join(map(str,current))))
                return
            last=current[-1]
            if 0<=last+k<=9:
                recurse(current+[last+k])
            if 0<=last-k<=9:
                recurse(current+[last-k])
        for start in range(1,10):
            recurse([start])
        return set(li)


        