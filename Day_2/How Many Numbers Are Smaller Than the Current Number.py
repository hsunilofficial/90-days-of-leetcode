# Day: 2 - Problem 1
# Problem: How Many Numbers Are Smaller Than the Current Number
## Description: For each number in the array, count how many numbers are smaller than it.
# Difficulty: Easy
# Time Taken: 5 minutes
# Hardest Hurdle: Finding a concise way to count smaller elements without writing nested loops explicitly.
# Pattern Used: Array Comparison / Brute Force Counting
# Submission Status: Accepted
# Key Learning: Python treats True as 1 and False as 0, so sum(n > x for x in nums) counts how many elements are smaller.

class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        return [sum(n > x for x in nums) for n in nums]