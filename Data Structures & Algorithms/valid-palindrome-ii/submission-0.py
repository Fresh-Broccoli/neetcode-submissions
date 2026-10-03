class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(s: str) -> bool:
            i, j = 0, len(s)-1
            output = len(s) == 1
            while i < j:
                if s[i] != s[j]:
                    break
                i, j = i+1, j-1
            else:
                output = True
            return output

        i, j = 0, len(s)-1
        output = len(s) == 1
        while i < j:
            if s[i] != s[j]:
                return is_palindrome(s[i:j]) or is_palindrome(s[i+1:j+1])
            i, j = i+1, j-1
        else:
            output = True
        return output
