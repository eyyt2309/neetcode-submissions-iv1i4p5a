class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        ch_map = defaultdict(int)
        longest = 0

        while r != len(s):
            if s[r] not in ch_map:
                ch_map[s[r]] = 1
                r += 1
            elif ch_map[s[r]] == 1:
                ch_map[s[l]] -= 1
                l += 1
            elif ch_map[s[r]] == 0:
                ch_map[s[r]] += 1
                r += 1

            print("Left:", l)
            print("Right:", r)

            curr = r - l
            print(curr)
            longest = curr if curr > longest else longest

        return longest

            

