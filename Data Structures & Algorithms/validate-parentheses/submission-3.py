class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2==1:
            return False
        open_to_close = {"(":")", "[":"]", "{":"}"}
        stack = []
        if s[0] not in open_to_close:
            return False
        for a in s:
            if a in open_to_close:
                stack.append(a)
            else:
                if len(stack) > 0:
                    if open_to_close[stack[-1]] == a:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        return len(stack) == 0