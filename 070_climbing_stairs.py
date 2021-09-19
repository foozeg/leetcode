#70. Climbing Stairs

class Solution:
    def climbStairs(self, n: int) -> int:
        prev = 1
        last = 1
        
        for _ in range(n-1):
            prev, last = last, prev + last
        return last
      
#Result:
#Runtime: 32 ms, faster than 58.56% of Python3 online submissions for Climbing Stairs.
#Memory Usage: 14 MB, less than 97.83% of Python3 online submissions for Climbing Stairs.
