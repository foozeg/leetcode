#198. House Robber

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) > 2:
            for i in range(len(nums)-3, -1, -1):
                print(i)
                nums[i] = max([j + nums[i] for j in nums[i+2:]])
            return max(nums[:2])
        else:
            return max(nums)
          
#Result:
#Runtime: 40 ms, faster than 31.53% of Python3 online submissions for House Robber.
#Memory Usage: 14.5 MB, less than 19.15% of Python3 online submissions for House Robber.
