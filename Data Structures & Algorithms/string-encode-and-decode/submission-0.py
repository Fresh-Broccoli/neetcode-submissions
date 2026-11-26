class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for s in strs:
            output += str(len(s)) + "#" + s
        return output

    def decode(self, s: str) -> List[str]:
        print(s)
        output = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            #print("i:", i)
            #print("j:", j)
            l = int(s[i:j])
            #l = s[i:j]
            #print(l)
            output.append(s[j+1:j+1+l])
            i = j+1+l
        return output