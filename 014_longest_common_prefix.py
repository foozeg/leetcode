#

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output = ""
        for chars in zip(*strs):
            if chars.count(chars[0]) == len(chars):
                output += chars[0]
            else:
                break
        return output
#Result
#Runtime: 36 ms, faster than 58.81% of Python3 online submissions for Longest Common Prefix.
#Memory Usage: 14.3 MB, less than 81.69% of Python3 online submissions for Longest Common Prefix.
