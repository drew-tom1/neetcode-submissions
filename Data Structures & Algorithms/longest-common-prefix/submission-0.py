class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pref = strs[0]
        
        for word in strs:
            while not word.startswith(pref):
                pref = pref[:len(pref) - 1]
            



        return pref
        