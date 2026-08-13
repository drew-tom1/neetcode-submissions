class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)

        nums = sorted(nums)
        seen = set()
        sequence = []
        sequence.append(nums[0])
        longest_seq = 0

        for i in range(1, len(nums)):
            if nums[i] not in seen: 
                if sequence and sequence[-1] == (nums[i] - 1):
                    sequence.append(nums[i])
                else:
                    sequence = [nums[i]]
            seen.add(nums[i])
            longest_seq = max(longest_seq, len(sequence))
            

        return longest_seq
        