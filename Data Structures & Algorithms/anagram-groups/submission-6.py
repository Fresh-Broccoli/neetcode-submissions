class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Convert strs to anagrams (List representation where list has a length of 26 corresponding with each alphabet character)

        Convert anagram to string then collect the string as a key in a dictionary, and value becomes original string
        corresponding with the string representation of the anagrams
        """

        def convert_to_anagram(string: str) -> str:
            """
            Given a string, convert to anagram using list representation.
            Returns anagram as a string concatenated with a whitespace delimiter

            Complexity: O(string)
            """
            output = [0 for _ in range(26)]
            for c in string:
                output[ord(c)-97] += 1
            return " ".join([str(o) for o in output])

        output = {}

        for i in range(len(strs)):
            anagram = convert_to_anagram(strs[i])
            if anagram in output:
                output[anagram].append(strs[i])
            else:
                output[anagram] = [strs[i]]
        return [lst for lst in output.values()]