class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        a, b, c, = False, False, False
        
        for triplet in triplets:
            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                continue

            for j in range(len(triplets[0])):
                if triplet[j] == target[0] and j == 0:
                    a = True
                if triplet[j] == target[1] and j == 1:
                    b = True
                if triplet[j] == target[2] and j == 2:
                    c = True

        return a and b and c
