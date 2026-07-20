class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # start at the last index, m + n - 1
        # if last index of num2 >= last index of num1, fill in last spot of nums1
        # with num2. otherwise, fill in num1 and replace former nums1 with 0.
        #decrement index of index2 always
        index1 = m-1
        index2 = n-1     
        j = m + n -1
        while index1 >= 0 and index2 >= 0:
            if nums2[index2] >= nums1[index1]:
                nums1[j] = nums2[index2]
                index2-=1
            else:
                nums1[j] = nums1[index1] 
                index1-=1
            j-=1 #always decrease this
        if index1 < 0:
            nums1[0: index2+1] = nums2[0: index2+1]
        return nums1
