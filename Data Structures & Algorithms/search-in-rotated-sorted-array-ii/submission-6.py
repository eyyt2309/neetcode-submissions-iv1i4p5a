class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2

            if nums[mid] == target:
                return True

            if nums[mid] == nums[r]:
                r -= 1
        
            elif nums[mid] >= nums[r]: # left of mid is sorted
                if nums[l] <= target < nums[mid]: # if target between mid and left
                    r = mid
                else: # target is on right of mid
                    l = mid + 1

            elif nums[mid] <= nums[r]: # right of mid is sorted
                if nums[mid] < target <= nums[r]: # if target between mid and right
                    l = mid + 1
                else: # target is on left of mid
                    r = mid 

        return False

