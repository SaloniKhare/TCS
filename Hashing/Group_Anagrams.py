from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        amp=defaultdict(list)
        for word in strs:
            st="".join(sorted(word))
            amp[st].append(word)
        return list(amp.values())
