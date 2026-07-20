class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closing = { ")" : "(", "]" : "[", "}" : "{" }

        for c in s:
            #if it is a closing paranthesis
            if c in closing:
                #if not empty stack and top of stack matches
                if stack and stack[-1] == closing[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        if not stack:
            return True
        else:
            return False
