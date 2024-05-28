count=0
class Solution:
    def climbStairs(self, n: int) -> int:
        global count
        def fibonacci(n):
            a=0
            b=1
            c=0
            for i in range(0,n):
                c=a+b
                a=b
                b=c
            return c
        k=fibonacci(n)
        return k