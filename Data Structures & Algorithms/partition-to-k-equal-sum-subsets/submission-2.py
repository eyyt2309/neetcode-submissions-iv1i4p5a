class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        dp = {}
        parts = total // k
        if parts * k != total: # unable to have integer parts
            return False

        n = len(nums)
        bitmask = [0 for _ in range(n)] # track integers used

        def dfs(curr, sets, m):
            if m == n and sets == 0:
                return True
            if (tuple(bitmask), sets) in dp:
                return dp[(tuple(bitmask), sets)]
            
            found = False
            for i in range(n):
                if bitmask[i] == 0 and curr + nums[i] == parts: # possible subset found
                    bitmask[i] = 1
                    found = found or dfs(0, sets - 1, m + 1)
                    bitmask[i] = 0
                elif bitmask[i] == 0 and curr + nums[i] < parts:
                    bitmask[i] = 1
                    found = found or dfs(curr + nums[i], sets, m + 1)
                    bitmask[i] = 0
            dp[(tuple(bitmask), sets)] = found
            return found

        return dfs(0, k, 0)
            

            
        