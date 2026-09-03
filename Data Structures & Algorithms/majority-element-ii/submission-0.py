from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        num_count = Counter(nums)

        threshold = len(nums) // 3
        ans = []
        for num in num_count:
            if num_count[num] > int(threshold):
                ans.append(num)

        return ans