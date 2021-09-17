#35. Search Insert Position

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        if target in nums:
            return nums.index(target)
        
        length = len(nums)
        
        if target <= nums[0]:
            return 0
        
        if target == nums[-1]:
            return length-1
        
        if target > nums[-1]:
            return length

        index = length // 2
        step = index
        while True:
            if target > nums[index]:
                step = (step // 2) + (step % 2)
                index += step
            elif target < nums[index-1]:
                step = (step // 2) + (step % 2)
                index -= step
                
            else:
                return index
#Result:
#Runtime: 52 ms, faster than 54.20% of Python3 online submissions for Search Insert Position.
#Memory Usage: 15 MB, less than 54.14% of Python3 online submissions for Search Insert Position.

class Solution2:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        if target in nums:
            return nums.index(target)
        
        if target < nums[0]:
            return 0
        
        if target > nums[-1]:
            return len(nums)
        
        for i in range(len(nums)):
            if target > nums[i] and target < nums[i+1]:
                return i+1
#Result
#Runtime: 94 ms, faster than 5.69% of Python3 online submissions for Search Insert Position.
#Memory Usage: 15.1 MB, less than 22.60% of Python3 online submissions for Search Insert Position.

#after checking others' solutions:
class Solution3:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        length = len(nums)
        
        if target <= nums[0]:
            return 0
        
        if target == nums[-1]:
            return length-1
        
        if target > nums[-1]:
            return length

        index = length // 2
        while True:
            if target == nums[index]:
                return index
            if target > nums[index]:
                index += 1
            elif target <= nums[index-1]:
                index -= 1
            else:
                return index
#Result:
#Runtime: 59 ms, faster than 29.12% of Python3 online submissions for Search Insert Position.
#Memory Usage: 14.8 MB, less than 99.06% of Python3 online submissions for Search Insert Position.
