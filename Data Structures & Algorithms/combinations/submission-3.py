class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = list()
        digits = [0 for _ in range(n)]

        def getCombination(nums, arr, start):
            # if 1 combination is obtained, return
            if nums == k:
                ans.append(arr.copy())
                return
            
            for i in range(start, n):
                if digits[i] == 0: # current digit not used in combination
                    arr.append(i + 1)
                    digits[i] = 1
                    getCombination(nums + 1, arr, i)
                    digits[i] = 0
                    arr.pop()
        arr = []
        getCombination(0, arr, 0)
        return [list(t) for t in ans]


            