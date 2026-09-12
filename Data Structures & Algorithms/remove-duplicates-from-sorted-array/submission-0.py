class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        last_sorted = 0 # idx to represent the last sorted number
        i = 1
        k = 1
        while i < n:
            if nums[i] > nums[last_sorted]:
                nums[last_sorted + 1], nums[i] = nums[i], nums[last_sorted + 1] # swap the two number
                last_sorted += 1
                i += 1
                k += 1
            else:
                i += 1
        return k      