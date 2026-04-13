class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashmap = {}
        
        for s in strs:
            key = tuple(self.getCharCount(s))
            if key not in hashmap:
                hashmap[key] = [s]
            else:
                hashmap[key].append(s)

        return list(hashmap.values())

    def getCharCount(self, s):
        count = [0] * 26

        for ch in s:
            index = ord(ch) - ord('a')
            count[index] += 1

        return count
