class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0 #pos of input string

        while i < len(s):
            j = i
            
            #finding integer from string
            while s[j] != '#': #to find the # character
                j+=1
            length = int(s[i:j]) #length of integer

            i = j + 1 #start of new word
            j = i + length #end of new word + 1
            res.append(s[i:j])
            i = j #next integer
        return res
