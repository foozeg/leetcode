#9. Palindrome Number

#Let's try solution with converting x to string
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x == 0:
            return True
        if x < 0 or (x % 10) == 0:
            return False
        x_str = str(x)
        if x_str == x_str[::-1]:
            return True
        else:
            return False
        
