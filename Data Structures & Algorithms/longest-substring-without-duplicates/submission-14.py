class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_to_index = {}
        start = 0
        longest = 1 if len(s) > 0 else 0
        for i in range(len(s)):
            if s[i] not in char_to_index:
                # If the list is not already in the dict, add it
                char_to_index[s[i]] = i
            else:
                # Otherwise, there are 2 possibilities:
                # 1. This character is a repetition in the current
                #    substring. Update longest, set start to the next
                #    character, then update the dictionary with the
                #    index of this character
                # 2. This character is not a repetition because its
                #    index is before variable start. In this case,
                #    just update the index.
                if start > char_to_index[s[i]]:
                    char_to_index[s[i]] = i
                else:
                    longest = max(longest, i-start)
                    start = char_to_index[s[i]] + 1
                    char_to_index[s[i]] = i
        longest = max(longest, len(s)-start)
        return longest