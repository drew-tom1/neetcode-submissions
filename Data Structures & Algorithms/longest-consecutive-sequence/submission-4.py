class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        num_set = set(nums)

        longest_seq = 0

        for num in num_set:
            if num - 1 not in num_set:
                length = 1
                next_num = num + 1
                while next_num in num_set:
                    length += 1
                    next_num += 1
                longest_seq = max(longest_seq, length)


        return longest_seq
        