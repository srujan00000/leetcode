class Solution:
    def strStr(self, h: str, n: str) -> int:
        for i in range(len(h)+1-len(n)):
            if h[i:i+len(n)]==n:
                return i
        return -1



        