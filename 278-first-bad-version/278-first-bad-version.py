# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        h=n
        l=0
        while l<=h:
            m=(l+h)//2
            if isBadVersion(m)==True:
                h = m-1
            else:
                l = m+1
        return l