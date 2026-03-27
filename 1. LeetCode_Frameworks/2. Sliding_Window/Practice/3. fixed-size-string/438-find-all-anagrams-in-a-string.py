class Solution:
    def findAnagrams(self, s, p):
        from collections import Counter

        if len(p) > len(s):
            return []
        
        p_count = Counter(p)
        window = Counter(s[:len(p)])
        result = []

        if window == p_count:
            result.append(0)
        
        for r in range(len(p), len(s)):
            l = (r - len(p))
            window[s[r]] += 1
            window[s[l]] -= 1

            if window[s[l]] == 0:
                del window[s[l]]

            if window == p_count:
                result.append(l + 1)

        return result