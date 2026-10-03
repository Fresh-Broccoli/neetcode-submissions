class Solution:
    def calPoints(self, operations: List[str]) -> int:
        mem = []
        for o in operations:
            if o == "+":
                mem.append(mem[-1]+mem[-2])
            elif o == "C":
                mem.pop()
            elif o == "D":
                mem.append(mem[-1]*2)
            else:
                mem.append(int(o))
        return sum(mem)
