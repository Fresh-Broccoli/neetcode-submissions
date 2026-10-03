class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ds, dt = self.get_char_count(s), self.get_char_count(t)
        return ds == dt

    def get_char_count(self, s,):
        d = {}
        for n in s:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1
        return d