class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def to_map(s):
            hmap = {}
            for c in s:
                if c in hmap:
                    hmap[c] += 1
                else:
                    hmap[c] = 1
            return hmap
        smap, tmap = to_map(s), to_map(t)
        return smap == tmap