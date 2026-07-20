from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_dict = defaultdict(list) #means it takes a list
        for s in strs:
            count = [0]*26
            for char in s: #idea is to use an array of 0 to 26 letters as dict key
                count[ord(char) - ord('a')] +=1
            key = tuple(count)
            anagrams_dict[key].append(s)
        return list(anagrams_dict.values())
        