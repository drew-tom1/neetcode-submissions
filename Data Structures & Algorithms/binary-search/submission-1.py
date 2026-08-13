class Solution:
    def search(self, nums: List[int], target: int) -> int:
        end = len(nums) - 1 # right side
        start = 0 # left side
        mid = 0 # initializing the middle variable

        while start <= end:
            mid = (end + start) // 2 # getting the middle

            if nums[mid] > target:
                end = mid - 1
            elif nums[mid] < target:
                start = mid + 1
            else:
                return mid
        return -1


        