# Day: 1 - Problem 3
# Problem: Set Mismatch
# Difficulty: Easy
# Time Taken: 6 minutes
# Hardest Hurdle: Understanding how to detect the duplicated and missing number using sums.
# Pattern Used: Hash Set / Mathematical Sum Difference
# Submission Status: Accepted
# Key Learning: Using a set removes duplicates, allowing comparison of sums to identify repeated and missing numbers.

class Solution(object):
    def findErrorNums(self, nums):
        s = set(nums)
        return [sum(nums) - sum(s), sum(range(1, len(nums)+1)) - sum(s)]