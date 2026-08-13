class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter1 = Counter(s)
        counter2 = Counter(t)

        lst1 = list(counter1.most_common())
        lst2 = list(counter2.most_common())

        lst1.sort()
        lst2.sort()

        return lst1 == lst2
        