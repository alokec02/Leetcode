class Solution:
    def minLength(self, s: str) -> int:
        stack = [None]
        for c in s:
            if stack[-1] == 'A' and c == 'B': stack.pop()
            elif stack[-1] == 'C' and c in 'D': stack.pop()
            else: stack.append(c)
        return len(stack) - 1    