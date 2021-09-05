#9. Palindrome Number

#Let's try solution with converting x to string
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x == 0:
            return True
        #negative and round numbers are not polindromes
        if x < 0 or (x % 10) == 0:
            return False
        x_str = str(x)
        #getting inverted sequence as x_str[::-1]
        if x_str == x_str[::-1]:
            return True
        else:
            return False

#Results
#Runtime: 64 ms, faster than 56.65% of Python3 online submissions for Palindrome Number.
#Memory Usage: 14.2 MB, less than 76.99% of Python3 online submissions for Palindrome Number.

#Lets' try solution without string operations
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x == 0:
            return True
        if x < 0 or (x % 10) == 0:
            return False
        if x == self.reverse(x):
            return True
        else:
            return False

    def reverse(self, x: int) -> int:
        rev = 0
        while x != 0:
            pop = x % 10
            x = int(x/10)
            rev = rev * 10 + pop
        return rev
#Result:
#Runtime: 64 ms, faster than 56.65% of Python3 online submissions for Palindrome Number.
#Memory Usage: 14.2 MB, less than 48.82% of Python3 online submissions for Palindrome Number.
        
