from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dt = defaultdict(list)

        for i, num in enumerate(nums):
            dt[num].append(i)

            if dt[target - num]: # if none empty list
                if target - num == num:
                    if len(dt[target-num]) > 1:
                        return [dt[target-num][0], dt[target-num][1]]
                else:
                    return[dt[target-num][0], dt[num][0]]

    