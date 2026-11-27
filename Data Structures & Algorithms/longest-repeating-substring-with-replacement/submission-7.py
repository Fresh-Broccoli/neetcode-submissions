class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = 0
        char_tracker = {}
        max_freq = 0
        max_len = 0

        for j in range(len(s)):
            # Add the new character to the window
            char_tracker[s[j]] = char_tracker.get(s[j], 0) + 1

            # Track the highest frequency we've seen
            max_freq = max(max_freq, char_tracker[s[j]])

            # Number of replacements needed:
            # window length - frequency of most common character
            while (j - i + 1) - max_freq > k:
                char_tracker[s[i]] -= 1
                i += 1

            max_len = max(max_len, j - i + 1)

        return max_len