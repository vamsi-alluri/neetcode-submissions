class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_to_open = { ')' : '(', '}': '{', ']': '[' }

        for i in s:

            match i:
                case '{' | '(' | '[':
                    stack.append(i)
                case _:
                    if stack and close_to_open[i] == stack[-1]:
                        stack.pop()
                    else:
                        return False
        return True if stack == [] else False