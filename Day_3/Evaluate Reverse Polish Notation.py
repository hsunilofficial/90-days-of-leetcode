"""
Day 3 - Problem 1

Problem Solved: Evaluate Reverse Polish Notation
Platform: LeetCode
Difficulty: Medium

Concepts Used:
- Stack
- Expression evaluation
- Handling integer division (truncate toward zero)

Approach:
Used a stack to process tokens.
Numbers are pushed to the stack.
When an operator appears, pop the last two numbers, perform the operation, and push the result back.

Key Challenge:
Handling division correctly with negative numbers (truncate toward zero).

Final Performance:
Runtime: 0 ms (Beats 100%)
Memory: 13.49 MB (Beats 98%)

Time Taken: ~30 minutes

Pattern Learned:
Stack-based expression evaluation (Reverse Polish Notation)

Next Goal:
Practice more stack problems to strengthen pattern recognition.
"""

class Solution(object):
    def evalRPN(self, tokens):
        s=[]
        for t in tokens:
            if t not in "+-*/":
                s.append(int(t))
            else:
                b=s.pop()
                a=s.pop()
                if t=='+':
                    s.append(a+b)
                elif t=='-':
                    s.append(a-b)
                elif t=='*':
                    s.append(a*b)
                else:
                    res=abs(a)//abs(b)
                    s.append(res if a*b>=0 else -res)
        return s[0]
