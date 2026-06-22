class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        num_len = len(nums)
        nums.sort()
        print(nums)

        ans = []

        for l in range(0, num_len - 3):
            for r in range(l + 3, num_len):
                start = l + 1
                end = r - 1
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
