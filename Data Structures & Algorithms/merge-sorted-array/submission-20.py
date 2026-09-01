class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        s1, s2 = m - 1, n - 1

        """ nums1 = [10,20,20,40,0,0] """
        """ nums2 = [1,2]             """
        last = len(nums1) - 1

        while s1 >= 0 and s2 >= 0:
            if nums1[s1] > nums2[s2]:
                nums1[last] = nums1[s1]
                s1 -= 1
                last -=1 
            else:
                nums1[last] = nums2[s2]
                s2 -= 1
                last -= 1
        
        while s1 >= 0:
            nums1[last] = nums1[s1]
            last -= 1
            s1 -= 1
        while s2 >= 0:
            nums1[last] = nums2[s2]
            last -= 1
            s2 -=1
