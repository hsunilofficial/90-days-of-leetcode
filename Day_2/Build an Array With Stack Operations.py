# Day: 2 - Problem 3
# Problem: Build an Array With Stack Operations
# Difficulty: Medium
# Time Taken: 8 minutes
# Hardest Hurdle: Understanding when to discard numbers from the stream using "Pop" while simulating stack operations.
# Pattern Used: Stack Simulation / Sequential Processing
# Submission Status: Accepted
# Performance:
#   Runtime: 0 ms (Beats 100%)
#   Memory: 12.32 MB (Beats ~83%)
# Key Learning: Simulating the stream 1..n with Push and Pop operations helps construct the target array efficiently.

class Solution(object):
    def buildArray(self, target, n):
        res = []
        j = 0

        for i in range(1, n + 1):
            if j == len(target):
                break

            res.append("Push")

            if i == target[j]:
                j += 1
            else:
                res.append("Pop")

        return res