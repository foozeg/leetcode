#13. Roman to Integer

class Solution1:
    def romanToInt(self, s: str) -> int:
        switch = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        
        int_array = []
        for i in range(len(s)):
            number = switch[s[i]]
            if i != len(s)-1:
                if number is 1 and (s[i+1] == 'V' or s[i+1] == 'X'):
                    number *= -1
                elif number is 10 and (s[i+1] == 'L' or s[i+1] == 'C'):
                    number *= -1
                elif number is 100 and (s[i+1] == 'D' or s[i+1] == 'M'):
                    number *= -1
            int_array.append(number)
            
        return sum(int_array)
#Result
#Runtime: 77 ms, faster than 10.22% of Python3 online submissions for Roman to Integer.
#Memory Usage: 14.4 MB, less than 26.93% of Python3 online submissions for Roman to Integer.

#After picking into solutions on leetcode
class Solution2:
    def romanToInt(self, s: str) -> int:
        switch = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        
        int_array = []
        for i in range(len(s)):
            number = switch[s[i]]
            if i != len(s)-1:
                next_number = switch[s[i+1]]
                #Roman numbers are always in descending order unless one is negative
                if (number < next_number):
                    number *= -1
            int_array.append(number)
        
        return sum(int_array)
#Result
#Runtime: 52 ms, faster than 48.56% of Python3 online submissions for Roman to Integer.
#Memory Usage: 14.3 MB, less than 58.67% of Python3 online submissions for Roman to Integer.
