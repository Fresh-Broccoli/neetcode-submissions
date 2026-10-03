class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        alphabet = list(map(chr, range(97, 123)))
        alpha_to_number = {alpha:n for n, alpha in enumerate(alphabet)}
        def to_str(s):
            o = [0]*26
            for i in range(len(s)):
                o[alpha_to_number[s[i]]] += 1
            print(o)
            return '-'.join([str(n) for n in o])
        
        output = {}
        for s in strs:
            lst = to_str(s)
            #print(lst)
            if lst in output:
                output[lst].append(s)
            else:
                output[lst] = [s]
        return list(output.values())