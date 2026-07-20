class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count the frequency of each number
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)  
            # .get(num, 0) means "if num is not in dictionary, default to 0"
            # so we increment frequency of num each time it appears

        # Step 2: Create buckets where index = frequency
        # freq[i] will hold a list of numbers that appear exactly i times
        freq = [[] for i in range(len(nums) + 1)]  
        # Why len(nums)+1? Because max frequency any number can have = len(nums)

        # Step 3: Fill the buckets
        for num, cnt in count.items():
            freq[cnt].append(num)
            # Example: if num=5 appeared 3 times → freq[3].append(5)

        # Step 4: Build result by iterating buckets in reverse
        result = []
        for i in range(len(freq) - 1, 0, -1):  
            # start from highest frequency down to 1
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result
                    # stop once we collected k most frequent elements
