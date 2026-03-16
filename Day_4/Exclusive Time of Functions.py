"""
Day 4

Solved: Exclusive Time of Functions.
Time Taken= ~25 minutes
Concept: Stack simulation
Idea: Track active functions using a stack and compute exclusive runtime from logs.

Key learning:

1.When a function starts, pause the current one and push the new function to the stack.
2.When a function ends, calculate its runtime and resume the previous function.

Result:
 Accepted - 120 / 120 test cases
 Runtime: 18 ms (Beats 75.19%)
Memory: 12.33 MB (Beats 93.85%)
"""

class Solution(object):
    def exclusiveTime(self, n, logs):
        res = [0]*n
        stack = []
        prev = 0
        
        for log in logs:
            i, typ, t = log.split(":")
            i, t = int(i), int(t)
            
            if typ == "start":
                if stack:
                    res[stack[-1]] += t - prev
                stack.append(i)
                prev = t
            else:
                res[stack.pop()] += t - prev + 1
                prev = t + 1
                
        return res