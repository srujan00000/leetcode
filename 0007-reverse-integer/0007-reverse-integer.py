class Solution:
    def reverse(self, x: int) -> int:
        flag=0
        if x<0:
            flag=1
            x=x*-1
        num=0
        while x>0:
            k=x%10
            num=num*10+k
            x=x//10
        if flag:
            num=num*-1
        return num if num in range(-2**31, 2**31) else 0