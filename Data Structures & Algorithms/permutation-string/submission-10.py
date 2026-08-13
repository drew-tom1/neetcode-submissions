class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # if s1 longer than s2, permutation cannot exist
        if len(s1) > len(s2):
            return False

        win_size = len(s1)
        s1_ct = Counter(s1)
        s2_ct = Counter()

        for i in range(win_size):
            s2_ct[s2[i]] += 1

            if s2_ct == s1_ct:
                return True

        for i in range(win_size, len(s2)):
            s2_ct[s2[i]] += 1

            outgoing = i - win_size
            s2_ct[s2[outgoing]] -= 1
            
            
            if s2_ct == s1_ct:
                return True
            
            
            

        return False
            
        