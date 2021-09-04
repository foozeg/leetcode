#7. Reverse Integer

#Let's try to solve it via inverting string
class Solution:
    def reverse(self, x: int) -> int:
        neg_flag = 1
        #need to remember if value is negative
        if x < 0:
            neg_flag = -1
        x_abs = abs(x)
        #here is inversion of numbers sequence
        result = int(str(x_abs)[::-1])
        #checking if result value fits integer
        if result >= 0x7fffffff:
            return 0
        result *= neg_flag
        return result
        
#Result:
#Runtime: 28 ms, faster than 89.21% of Python3 online submissions for Reverse Integer.
#Memory Usage: 14.4 MB, less than 12.02% of Python3 online submissions for Reverse Integer.
#Most likely hight memory usage is consequence of operations with string
