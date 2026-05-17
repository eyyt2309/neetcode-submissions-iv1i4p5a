class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        hashmap = {}

        for num in hand:
            if num not in hashmap:
                hashmap[num] = 1
            else:
                hashmap[num] += 1
        
        for num in hand:
            if hashmap.get(num, 0) >= 1:
                count = 1
                hashmap[num] -= 1
                while count != groupSize:
                    if hashmap.get(num + 1, 0) >= 1:
                        hashmap[num + 1] -= 1
                        num += 1
                        count += 1
                    else:
                        return False
            else:
                continue

        return True
