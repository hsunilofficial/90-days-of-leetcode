# Day: 1 - Problem 2
# Problem: Max Consecutive Ones
# Difficulty: Easy
# Time Taken: 4 minutes
# Hardest Hurdle: Resetting the counter when encountering 0 while tracking the maximum streak.
# Pattern Used: Array Traversal with Running Count
# Submission Status: Accepted
# Key Learning: Maintaining a running counter while traversing an array helps detect consecutive patterns efficiently.

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        c = m = 0
        for i in nums:
            c = c + 1 if i else 0
            m = max(m, c)
        return m