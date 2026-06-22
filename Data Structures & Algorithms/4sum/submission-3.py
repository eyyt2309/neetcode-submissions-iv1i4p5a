class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        num_len = len(nums)
        nums.sort()

        ans = []

        for l in range(0, num_len - 3):
            if l > 0 and nums[l] == nums[l - 1]:
                continue
            for r in range(l + 1, num_len - 2):
                if r > l + 1 and nums[r] == nums[r - 1]:
                    continue
                start = r + 1
                end = num_len - 1
                while start < end:
                    total = nums[l] + nums[r] + nums[start] + nums[end]
                    if total == target:
                        if [nums[l], nums[start], nums[end], nums[r]] not in ans:
                            ans.append([nums[l], nums[start], nums[end], nums[r]])
                        start += 1
                    elif total < target:
                        start += 1
                    elif total > target:
                        end -= 1

        return ans
