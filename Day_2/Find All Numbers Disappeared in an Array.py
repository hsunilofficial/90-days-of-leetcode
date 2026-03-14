# Day: 2 - Problem 2
# Problem: Find All Numbers Disappeared in an Array
# Difficulty: Easy
# Time Taken: 7 minutes
# Hardest Hurdle: Understanding how index marking can track visited numbers without extra space.
# Pattern Used: Array Index Marking
# Submission Status: Accepted
# Key Learning: Numbers map to indices (value-1). Marking indices negative allows detection of missing numbers.

class Solution(object):
    def findDisappearedNumbers(self, nums):
        for n in nums:
            nums[abs(n)-1] = -abs(nums[abs(n)-1])
        return [i+1 for i, n in enumerate(nums) if n > 0]