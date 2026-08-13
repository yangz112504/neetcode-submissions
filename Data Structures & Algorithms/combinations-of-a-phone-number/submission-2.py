class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []

        totalCombos = []
        currString = []
        maxLetters = len(digits)

        numToStr = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        def helper(index, currString, totalCombos):
            if index == maxLetters:
                totalCombos.append("".join(currString))
                return
            
            charSet = numToStr[digits[index]]
            for letter in charSet:
                currString.append(letter)
                helper(index+1,currString,totalCombos)
                currString.pop()

        helper(0,currString, totalCombos)
        return totalCombos