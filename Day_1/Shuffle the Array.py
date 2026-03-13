# Day: 1 - Problem 1
# Problem: Shuffle the Array
# Difficulty: Easy
# Time Taken: 6 minutes
# Hardest Hurdle: Initially had a syntax error and variable mismatch ("num" vs "nums").
# Pattern Used: Array Traversal / Index Manipulation / List Comprehension
# Submission Status: Accepted
# Key Learning: Python list comprehension can interleave elements efficiently using index pairs.

class Solution(object):
    def shuffle(self, nums, n):
        return [nums[j] for i in range(n) for j in (i, i+n)]