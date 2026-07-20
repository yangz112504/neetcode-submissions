class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        paranMap = {'(': ')', '{': '}', '[': ']'}
        for c in s:
            if c not in paranMap:
                if len(stack) == 0:
                    return False
                opener = stack.pop()
                if paranMap[opener] == c:
                    continue
                else:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0
        