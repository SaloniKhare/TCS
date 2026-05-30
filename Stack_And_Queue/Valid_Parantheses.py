class Solution:
    def isValid(self, s: str) -> bool:
        st=[]

        for i in range(len(s)):

            if s[i] in {"(","{","["}:
                st.append(s[i])
            else:
                if not st:
                    return False
                l=st[-1]
                h=s[i]
                if (l=="(" and h==")") or (l=="{" and h=="}") or (l=="[" and h=="]"):
                    st.pop()
                else:
                    return False
        return len(st)==0
