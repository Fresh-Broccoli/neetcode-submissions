class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        d, h, m = {}, 0, 0

        for i in range(len(s)):
            #print("d:", d)
            # Check if we have seen this letter
            if s[i] in d:
                # Either with it not being in the dictionary,
                # or its last index is lower than the current.
                # If this is the case, count the current length,
                # compare with m (update if greater), then update
                # h
                if d[s[i]] >= h:
                    c = i - h
                    print("c:", c)
                    m = c if c > m else m
                    h = d[s[i]] + 1
                    print("m:",m)
            d[s[i]] = i
            print("d:", d)
        c = len(s) - h #if h != 0 else len(s)
        print("c:", c)
        print("m:", m)
        return c if c > m else m

            
                




def old_solution():
    d, h, m = {}, 0, 0
    for i in range(len(s)):
        print("letter:", s[i])
        
        if s[i] in d:
            # Update h
            h = d[s[i]] + 1
            
            if d[s[i]] < h:
                d[s[i]] = i

            # Get count
            c = i - h
            print("c:", c)
            # Check if m is less than c, if so, set m to c
            m = c if m < c else m

            print("h:", h)
            print("m:", m)
        else:
            d[s[i]] = i
        print("d:", d)
    c = len(s) - h
    return m if m > c else c