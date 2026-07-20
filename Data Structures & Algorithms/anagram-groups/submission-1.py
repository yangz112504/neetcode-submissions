from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myDict = defaultdict(list)
        for word in strs:
            countKey = [0] * 26
            for letter in word:
                countKey[ord(letter) - ord('a')]+=1
            key = tuple(countKey)
            myDict[key].append(word)
        return list(myDict.values())