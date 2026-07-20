class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for index, value in enumerate(nums):
            if index > 0 and value == nums[index-1]:
                continue
            l = index + 1
            r = len(nums)-1
            while l < r:
                threeSum = nums[l] + value + nums[r]
                if threeSum > 0:
                    r-=1
                if threeSum < 0:
                    l+=1
                if threeSum == 0:
                    res.append([value, nums[l],nums[r]])
                    l+=1
                    r-=1
                    while nums[l] == nums[l-1] and l < r:
                        l+=1
        return res
            