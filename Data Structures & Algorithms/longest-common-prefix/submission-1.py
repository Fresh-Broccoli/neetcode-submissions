class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        i = 0

        # Find the length of the shortest string
        l = min([len(s) for s in strs])
        while i < l:
            if len(set([s[i] for s in strs]))==1:
                prefix += strs[0][i]
                i += 1
            else:
                break
        return prefix