class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i=j=0
        st=[]
        count=total=0
        while j<len(s):
            if s[j] in st:
                st.pop(0)
                i+=1
            else:
                st.append(s[j])
                j+=1
            if len(st)>total:
                total=len(st)
        return total
                
                
                