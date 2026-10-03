class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        alphanumeric_map = {l:n for n,l in enumerate(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"])}
        def count_chars(string):
            out = [0 for _ in range(26)]
            for c in string:
                out[alphanumeric_map[c]] += 1
            return ",".join(str(n) for n in out)
        # O(m*n)
        counted = [count_chars(string) for string in strs]
        count_dict = {}
        for i, string in enumerate(counted):
            if string in count_dict:
                count_dict[string].append(strs[i])
            else:
                count_dict[string] = [strs[i]]
        return list(count_dict.values())