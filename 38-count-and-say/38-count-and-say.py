class Solution:
    def rec(self, s, n):
        
        count = 0
        ans = ''
        prev = ''
        i = 0
        print(f'n={n}')
        while i < len(s):
            
            if s[i] == prev:
                count +=1
            else:
                if count != 0:
                    ans += (str(count) + prev)
                count = 1
                prev = s[i]
            i+=1
        ans += (str(count)+prev)
        
        if n == 1:
            return ans
        else:
            return self.rec(ans, n-1)
    
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        return self.rec('1', n-1)