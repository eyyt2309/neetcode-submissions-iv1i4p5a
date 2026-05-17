class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hashmap = {}

        for i, ch in enumerate(s):
            if ch not in hashmap:
                hashmap[ch] = [i, i]
            else:
                hashmap[ch][1] = i
        print(hashmap)

        ans = []

        i = 0
        while i < len(s):
            ch, last = s[i], hashmap[s[i]][1]
            idx = i
            while idx != last:
                if s[idx] != ch and hashmap[s[idx]][1] > last:
                    ch = s[idx]
                    last = hashmap[s[idx]][1]
                idx += 1
            ans.append(last - i + 1)
            i = last + 1

        return ans