class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        totalCombos = []
        currString = ""
        maxLetters = len(digits)

        numToStr = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        def helper(index, currString, totalCombos):
            if index == maxLetters:
                totalCombos.append(currString)
                return
            
            charSet = numToStr[digits[index]]
            for letter in charSet:
                helper(index+1,currString + letter,totalCombos)
        
        if digits == "":
            return []

        helper(0,currString, totalCombos)
        return totalCombos