class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # nums in increasing order
        # remove duplicates so each number appears <= 2 times. order is same
        # with sorted array, that means if we increase a number by r
        # k is going to l + 1 bc of indexing
        l = 0
        seen = 1
        for r in range(1,len(nums)):
            if nums[r] == nums[l]:
                if seen < 2:
                    seen+=1
                    l+=1
                    nums[l] = nums[r]
                else:
                    continue
            else: # new number
                seen = 1
                l+=1
                nums[l] = nums[r]
        return l+1

                


        