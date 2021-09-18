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
