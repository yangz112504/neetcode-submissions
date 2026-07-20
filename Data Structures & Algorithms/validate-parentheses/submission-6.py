class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {")": "(", "}" : "{", "]" : "["}

        for char in s:
            if char not in hashmap:
                stack.append(char)
            else: #it's a closing bracket
                if stack and stack[-1] == hashmap[char]:
                    stack.pop()
                else:
                    return False 
        return len(stack) == 0
                    
        