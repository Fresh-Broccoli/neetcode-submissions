class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Anagrams can be checked by maintaining a fixed list of numbers,
        where the list size is the size of the alphabet, and the numbers
        are the number of times a character has appeared in the input.

        Because the alphabet is fixed, updating and comparisons are O(1).
        """

        def letter_to_index(l: str) -> int:
            """
            Given char l, return corresponding index number where:
                - l = "a" gives 0
                - l = "z" gives 25
            """
            return ord(l)-97

        # Initialise such that counts are 0 for both strings
        # O(1)
        #sa, ta = [0 for _ in range(26)], [0 for _ in range(26)]

        # Count strings
        def count_string(s: str) -> List[int]:
            # Initialise such that counts are 0 for all alphabets
            # O(1)
            sa = [0 for _ in range(26)]

            # Iterate over s, for each letter, find index and increment
            # by 1.
            # O(s)
            for l in s:
                index = letter_to_index(l)
                sa[index] += 1

            return sa

        # Return the comparison of the string representation between s and t:
        # O(s + t)
        return count_string(s) == count_string(t)
