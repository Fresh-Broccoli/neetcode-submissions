class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def create_dict(string):
            out = {}
            for c in string:
                if c in out:
                    out[c] += 1
                else:
                    out[c] = 1
            return out
        return create_dict(s) == create_dict(t)