class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Strips non alphanumeric characters and sets string to lowercase
        clean_s = ''.join(char for char in s if char.isalnum()).lower()
        return clean_s == clean_s[::-1]