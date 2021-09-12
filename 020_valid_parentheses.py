#20. Valid Parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        opens = ('(', '{', '[')
        closes = (')', '}', ']')
        sequence = []
        
        for i in s:
            #we track sequence op opening parentheses in sequence var
            if i in opens:
                sequence.append(opens.index(i))
            else:
                #if sequence starts with closes parentheses return false
                if len(sequence) == 0:
                    return False
                
                #we use .pop() to kick out last opened parenthesis and to compare it to currently closes
                closes_index = closes.index(i)
                if sequence.pop() != closes_index:
                    return False
        
        #if not all parentheses closed return false
        if len(sequence) > 0 :
            return False
        
        return True

#Results:
#Runtime: 32 ms, faster than 65.91% of Python3 online submissions for Valid Parentheses.
#Memory Usage: 14.3 MB, less than 63.75% of Python3 online submissions for Valid Parentheses.
