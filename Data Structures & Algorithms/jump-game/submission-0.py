class Solution:
    def canJump(self, nums: List[int]) -> bool:
        num_len = len(nums)

        goal_idx = num_len - 1

        start_idx = num_len - 2

        while goal_idx > 0:

            if start_idx == -1:
                return False
            
            if start_idx + nums[start_idx] >= goal_idx:
                goal_idx = start_idx
                start_idx = goal_idx - 1
            else:
                start_idx -= 1


        else:
            return True