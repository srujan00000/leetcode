class Solution:
    def isPalindrome(self, x: int) -> bool:
        dig=0
        num=x
        while num>0:
            dig=dig*10+num%10
            num=num//10
        return True if dig==x else False
        