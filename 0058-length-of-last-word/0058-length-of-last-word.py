class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n=len(s)-1
        while s[n]==" ":
            n-=1
        count=0
        while s[n]!=" ":
            count+=1
            if s[n]==" " or n==0:
                break
            n-=1
        return count
        