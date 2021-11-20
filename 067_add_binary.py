class Solution:
    def addBinary(self, a: str, b: str) -> str:
        c = int(a, base=2) + int(b, base=2)
        return str(bin(c))[2:]

#Runtime: 28 ms, faster than 92.77% of Python3 online submissions for Add Binary.
#Memory Usage: 13.9 MB, less than 99.96% of Python3 online submissions for Add Binary.
