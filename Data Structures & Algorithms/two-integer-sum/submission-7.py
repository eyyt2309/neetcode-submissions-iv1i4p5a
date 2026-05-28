class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i, num in enumerate(nums):
            if num not in hashmap:
                hashmap[num] = [i]
            else:
                hashmap[num].append(i)

        for num in hashmap:
            if (target - num) in hashmap:
                if target - num == num and len(hashmap[num]) > 1:
                    return hashmap[num][:2]
                elif target - num != num:
                    return hashmap[num] + hashmap[target - num]