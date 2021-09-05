#7. Reverse Integer

#Let's try to solve it via inverting string
class Solution1:
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

#Let's try to implement solution from the Leetcode with no string operations
class Solution2:
    def reverse(self, x: int) -> int:
        rev = 0
        neg_flag = 1
        #need to remember if value is negative
        if x < 0:
            neg_flag = -1
        x_abs = abs(x)
        while x_abs != 0:
            pop = x_abs % 10
            x_abs = int(x_abs/10)
            if (rev > 2147483647/10 or (rev == 2147483647 / 10 and pop > 7)): 
                return 0
            if (rev < -2147483648/10 or (rev == -2147483648 / 10 and pop < -8)):
                return 0
            rev = rev * 10 + pop
        return rev * neg_flag

#Result:
#Runtime: 32 ms, faster than 71.05% of Python3 online submissions for Reverse Integer.
#Memory Usage: 14.4 MB, less than 12.02% of Python3 online submissions for Reverse Integer.
#Not a big difference =\
