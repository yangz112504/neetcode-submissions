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
            while(s[j] != '#'):
                j+=1
            length = int(s[i:j]) #integer
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
        return res
