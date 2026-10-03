class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sl, tl = [0 for _ in range(26)], [0 for _ in range(26)]
        for i in range(len(s)):
            sl[ord(s[i])-97] += 1
            tl[ord(t[i])-97] += 1
        return ",".join([str(c) for c in sl]) == ",".join([str(c) for c in tl])