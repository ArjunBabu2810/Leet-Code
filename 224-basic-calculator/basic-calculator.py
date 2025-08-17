class Solution:
    def calculate(self, s: str) -> int:
        s=s.replace(" ",'')
        st = []
        num =0
        sign =1
        i=0

        result = 0
        while i < len(s):
            ch = s[i]
            if ch.isdigit():
                num = num*10 + int(ch)
            
            elif ch in "+-":
                result +=sign*num
                num =0
                sign = 1 if ch=='+' else -1
                
            elif ch == '(':
                st.append((result,sign))
                num =0
                sign =1
                result = 0
            elif ch == ')':
                result+=sign*num
                
                prevres,prevsign = st.pop()
                
                result = prevres+(prevsign*result)
                sign =1
                num=0
            
            i+=1
        return result + sign * num
