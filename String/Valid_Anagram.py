from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        return "".join(sorted(s))=="".join(sorted(t))


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts_s = defaultdict(int)
        for c in s:
            counts_s[c] += 1
        counts_t = defaultdict(int)
        for c in t:
            counts_t[c] +=1
        return counts_s == counts_t


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       return Counter(s) == Counter(t)       
