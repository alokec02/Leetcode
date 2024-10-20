class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        reduce = {
        '&': lambda x, y: x and y,
        '|': lambda x, y: x or y
        }
        stack = []
        opened = False
        for c in expression:
            if c in {'&', '|', '!', '('}:
                stack.append(c)
            elif c == 't':
                stack.append(True)
            elif c == 'f':
                stack.append(False)
            elif c == ')':
                arr = []
                while stack[-1] != '(':
                    arr.append(stack.pop())
                stack.pop()
                if stack[-1] in reduce:
                    op = stack.pop()
                    stack.append(functools.reduce(reduce[op], arr))
                elif stack[-1] == '!':
                    stack.pop()
                    stack.append(not arr[0])
        return stack[0]