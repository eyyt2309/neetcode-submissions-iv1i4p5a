class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        # rotate by n is the same as not doing anything

        k = k % n

        for _ in range(k):
            nums.insert(0, nums.pop())
        