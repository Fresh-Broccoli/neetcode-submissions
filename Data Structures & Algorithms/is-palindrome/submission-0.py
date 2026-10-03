class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s)-1
        ls = s.lower()
        while i < j:
            if not ls[i].isalnum():
                i+=1
                continue
            if not ls[j].isalnum():
                j-=1
                continue
            if ls[i] != ls[j]:
                return False
            i, j = i+1, j-1
        return True