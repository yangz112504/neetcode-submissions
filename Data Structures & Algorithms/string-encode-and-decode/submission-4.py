class Solution:

    def encode(self, strs: List[str]) -> str:
        # LENGTH | # | str
        res = []
        for word in strs:
            length = str(len(word))
            res.append(length+"#"+word)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
    
        index = 0
        while index < len(s):
            # find number
            numList = []
            while s[index] != "#":
                numList.append(s[index])
                index+=1
            wordLen = int("".join(numList))


            # build word
            index+=1
            currWord = []
            while wordLen > 0:
                currWord.append(s[index])
                index+=1
                wordLen-=1
            res.append("".join(currWord))
        
        return res
            

                
