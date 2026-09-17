class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        curr_a, curr_b, curr_c = 0, 0, 0
        for triplet in triplets:

            # skip triplets that
            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                continue
            
            curr_a = max(curr_a, triplet[0])
            curr_b = max(curr_b, triplet[1])
            curr_c = max(curr_c, triplet[2])

        if [curr_a, curr_b, curr_c] == target:
            return True
        return False