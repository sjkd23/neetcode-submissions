class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        for x in s:
            if stack:
                if x == ']' and stack[-1] == '[':
                    stack.pop()
                elif x == '}' and stack[-1] == '{':
                    stack.pop()
                elif x == ')' and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(x)
            else:
                stack.append(x)
        return not stack