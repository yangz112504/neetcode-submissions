class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for index, value in enumerate(nums):
            #skipping over duplicate values
            if index > 0 and value == nums[index-1]:
                continue
            #pointers
            l = index + 1
            r = len(nums) - 1
            #for each num in nums
            while l < r:
                threeSum = value + nums[l] + nums[r]
                if threeSum > 0:
                    r-=1
                if threeSum < 0:
                    l+=1
                if threeSum == 0:
                    res.append([value, nums[l], nums[r]])
                    l+=1
                    r-=1
                    while nums[l] == nums[l-1] and l < r:
                        l+=1
        return res 
            