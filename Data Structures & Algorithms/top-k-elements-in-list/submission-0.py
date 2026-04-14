class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        buckets = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            count[num] = count.get(num, 0 ) + 1

        for num, freq in count.items():
            buckets[freq].append(num)

        ans = []

        for freq in reversed(buckets):
            for num in freq:
                ans.append(num)
            if len(ans) == k:
                return ans
