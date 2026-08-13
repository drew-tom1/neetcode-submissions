class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        listCount = Counter(nums)
        top_k = []
        k_frequency = (listCount.most_common(k))
        for element, frequency in k_frequency:
            top_k.append(element)
        return top_k