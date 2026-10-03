class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l = len(word1) if len(word1) < len(word2) else len(word2)
        i = 1
        output = word1[0] + word2[0]
        while i < l:
            output = output + word1[i] + word2[i]
            i += 1
        return output + word1[i:] + word2[i:]