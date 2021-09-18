#509. Fibonacci Number

class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        return self.fib(n - 1) + self.fib(n - 2)
      
#Result
#Runtime: 916 ms, faster than 14.31% of Python3 online submissions for Fibonacci Number.
#Memory Usage: 14.3 MB, less than 40.34% of Python3 online submissions for Fibonacci Number.

class Solution2:
    mem = {0: 0, 1: 1}
   
    def fib(self, n: int) -> int:
        if n in self.mem:
            return self.mem[n]
        self.mem[n] = self.fib(n - 1) + self.fib(n - 2)       
        return self.mem[n]
#Result:
#Runtime: 28 ms, faster than 86.81% of Python3 online submissions for Fibonacci Number.
#Memory Usage: 14.2 MB, less than 40.34% of Python3 online submissions for Fibonacci Number.

#dynamic programming
class Solution3:
    def fib(self, n: int) -> int:
        a = 0
        b = 1
        for _ in range(n):
            a, b = b, a + b
        return a
    
#Result:
#Runtime: 32 ms, faster than 69.15% of Python3 online submissions for Fibonacci Number.
#Memory Usage: 14.3 MB, less than 8.50% of Python3 online submissions for Fibonacci Number.
