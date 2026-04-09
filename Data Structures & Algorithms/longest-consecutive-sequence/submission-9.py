class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        ans = 1

        num_set = set(map(int, nums))

        if len(nums) == 0:
            return 0

        for num in nums:
            temp_num = num
            length = 1

            if (temp_num + 1) not in num_set:
                continue
            else:
                while temp_num + 1 in num_set:
                    temp_num += 1
                    length += 1

                    if length > ans:
                        ans = length

        return ans

            




