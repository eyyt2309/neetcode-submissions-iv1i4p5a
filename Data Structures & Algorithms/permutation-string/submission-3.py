class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        char_map = {}
        for ch in s1:
            if ch not in char_map:
                char_map[ch] = 1
            else:
                char_map[ch] += 1

        index = 0
        window = 0

        while index < len(s2):
            check_map = {}

            if s2[window] not in char_map:
                index += 1
                window += 1
            else:
                while window < len(s2) and s2[window] in char_map:
                    if s2[window] not in check_map:
                        check_map[s2[window]] = 1
                    else:
                        check_map[s2[window]] += 1
                    
                    if check_map == char_map:
                        return True
                    window += 1

                index += 1
                window = index


        return False

        