from collections import defaultdict


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        start_end = defaultdict(list)

        for i, ch in enumerate(s):
            if not start_end[ch]:
                start_end[ch].append(i)
                start_end[ch].append(i)
            else:
                start_end[ch][1] = i

        size = 1
        ans = []
        max_idx = 0
        for i, ch in enumerate(s):
            max_idx = max(max_idx, start_end[ch][1])
            if max_idx == i:
                max_idx = max_idx + 1
                ans.append(size)
                size = 1
            else:
                size += 1
        return ans
