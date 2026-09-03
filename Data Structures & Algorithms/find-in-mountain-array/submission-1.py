class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()
        if n < 3:
            return -1

        l, r = 0, n - 1

        # find pivot:
        while l < r:
            mid = l + (r - l) // 2

            if mountainArr.get(mid) < mountainArr.get(mid + 1):
                l = mid + 1
            else:
                r = mid
        peak = l

        # check left side of peak first
        l, r = 0, peak
        while l <= r:
            mid = l + (r - l) // 2

            middle = mountainArr.get(mid)
            if middle == target:
                return mid
            elif middle < target:
                l = mid + 1
            else:
                r = mid - 1

        # check right side of peak 
        l, r = peak, n - 1
        while l <= r:
            mid = l + (r - l) // 2

            middle = mountainArr.get(mid)
            if middle == target:
                return mid
            elif middle < target:
                r = mid - 1
            else:
                l = mid + 1

        return -1
        