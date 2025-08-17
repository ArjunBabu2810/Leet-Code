class Solution:
    def balancedStringSplit(self, s: str) -> int:
        c=0
        b=0
        for i in s:
            if i == "R":
                c+=1
            if i == "L":
                c-=1
            if c == 0 :
                b+=1
        return b