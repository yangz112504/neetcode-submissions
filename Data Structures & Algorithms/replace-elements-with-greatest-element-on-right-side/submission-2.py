class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxNum = -1
        for i in range(len(arr)-1,-1,-1):
            temp = arr[i]
            arr[i] = maxNum
            maxNum = max(temp, maxNum)
        return arr
        