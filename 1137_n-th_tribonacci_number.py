#1137. N-th Tribonacci Number

class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        #t0
        a = 0
        #t1
        b = 1
        #t2
        c = 1
        #t1, t2 we have, so range is n - 2
        for _ in range(n-2):
            a, b, c = b, c, a+b+c
            print(c)
        return c

#Result:
#Runtime: 28 ms, faster than 82.97% of Python3 online submissions for N-th Tribonacci Number.
#Memory Usage: 14.2 MB, less than 70.13% of Python3 online submissions for N-th Tribonacci Number.
