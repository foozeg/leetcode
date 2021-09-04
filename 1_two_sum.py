# 1. Two Sum

#Let's try to solve it with recursive function. 
class Solution1: 
    step = 0
	#i'm using step as a shift counter for the first index
	#idea is to summarise all possible pairs and compare them to the target. Starting from the first element in the array
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(self.step+1, len(nums)):
            result = nums[self.step] + nums[i]
            if result == target:
                return [self.step, i]
        self.step += 1
		#if sum of any element with current element doesn't give target, then we shift to next element and execute function again
        solution = self.twoSum(nums, target)
        return solution
		
#Results:
#Runtime: 8334 ms, faster than 5.01% of Python3 online submissions for Two Sum.
#Memory Usage: 24.3 MB, less than 5.00% of Python3 online submissions for Two Sum.
#Result is far away from good

#Let's get rid of recursive function and sums on each step.
class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            diff = target - nums[i]
			#diff is the desired value to make target out of current i element
            sub_array = nums[i+1:]
            if diff in sub_array:
                index_of_diff = i + 1 + sub_array.index(diff)
                return [i, index_of_diff]

#Results:
#Runtime: 728 ms, faster than 35.39% of Python3 online submissions for Two Sum.
#Memory Usage: 14.8 MB, less than 92.43% of Python3 online submissions for Two Sum.
#Better now, but still far away from perfect
