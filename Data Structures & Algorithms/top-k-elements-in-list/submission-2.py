class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter1 = Counter(nums)
        top_k = []
        k_frequency = list(counter1.most_common(k))
        for element, frequency in k_frequency:
            top_k.append(element)
        return top_k
        