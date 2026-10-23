class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # brute force is to for every num to try all other triplet combos This is O(n^3) because we are iterating though 3 elements 
        nums.sort()
        res = []
        i = 0
        for i in range(len(nums)-2):
            fixedNum = nums[i]
            if fixedNum > 0:
                # because sorted, all remaining numbers positive
                break
            if i > 0 and fixedNum == nums[i-1]:
                continue # skipped duplicates
            l = i+1
            r = len(nums) - 1

            # set up 2 pointers
            while l < r:
                currSum = fixedNum  + nums[l] + nums[r]
                if currSum == 0:
                    res.append([fixedNum, nums[l],nums[r]])
                    r-=1
                    l+=1
                    while nums[l] == nums[l-1] and l < r:
                        l+=1 # skips duplicates

                elif currSum > 0:
                    r-=1
                else:
                    l+=1
        return res




       