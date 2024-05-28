class Solution:
    def addBinary(self, a: str, b: str) -> str:
        k=int(a,2)
        l=int(b,2)
        p=k+l
        def decimalToBinary(n):
            return bin(n).replace("0b","")
        f=decimalToBinary(p)
        return f