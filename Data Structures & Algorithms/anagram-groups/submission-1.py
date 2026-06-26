class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            sorted_string = "".join(sorted(s))
            groups[sorted_string].append(s)
        ans = []

        for key in groups:
            ans.append(groups[key])

        return ans