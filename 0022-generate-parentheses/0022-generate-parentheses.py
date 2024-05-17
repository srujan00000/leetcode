class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack=[]
        res=[]
        def gen(openN,closeN):
            if closeN==openN==n:
                res.append("".join(stack))
                return
            if openN<n:
                stack.append("(")
                gen(openN+1,closeN)
                stack.pop()
            if closeN<openN:
                stack.append(")")
                gen(openN,closeN+1)
                stack.pop()
        gen(0,0)
        return res        