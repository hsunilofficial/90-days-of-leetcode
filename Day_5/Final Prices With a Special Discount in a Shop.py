"""
Day 5

Problem Name: Final Prices With a Special Discount in a Shop
Difficulty: Easy

Approach Used:
- Main concept: Next Smaller or Equal Element
- Data structure: Monotonic Stack
- Key idea: Use a stack to track indices and apply discount when a smaller or equal price appears on the right

Key Learnings:
- Monotonic stack reduces time complexity from O(n²) to O(n)
- Storing indices instead of values helps update result directly
- Each element is pushed and popped at most once

Performance:
- Runtime: 0 ms (Beats 100%)
- Memory: 12.42 MB (Beats 73.18%)
- Time taken: ~25 minutes

Mistakes / Improvements:
- Initially thought of brute force approach
- Took time to recognize stack pattern

Pattern Recognized:
- Monotonic Stack (Next Smaller Element)
"""
class Solution:
    def finalPrices(self, prices):
        stack = []
        res = prices[:]   # copy of original prices
        
        for i in range(len(prices)):
            while stack and prices[i] <= prices[stack[-1]]:
                res[stack.pop()] -= prices[i]
            stack.append(i)
        
        return res