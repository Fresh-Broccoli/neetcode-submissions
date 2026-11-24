class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def convert_to_string_representation(st: str) -> str:
            # 26 items in list where 0th represents "a" and 25th represents "z"
            tr = [0]*26
            for s in st:
                tr[ord(s)-97] += 1
            return "-".join([str(t) for t in tr])

        sr = {}
        for st in strs:
            key = convert_to_string_representation(st)
            if key in sr:
                sr[key].append(st)
            else:
                sr[key] = [st]
        return list(sr.values())