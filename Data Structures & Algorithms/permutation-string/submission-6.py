class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # if s1 longer than s2, permutation cannot exist
        if len(s1) > len(s2):
            return False

        win_size = len(s1)
        s1_ct = Counter(s1)
        s2_ct = Counter()

        for i in range(len(s2)):
            s2_ct = Counter(s2[i : i + win_size])
            print(s2_ct)
            
            if s2_ct == s1_ct:
                return True
            
            
            

        return False
            
        