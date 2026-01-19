class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        result = 0
        max_val = 0  # max(nums[i]) for i < j
        max_diff = 0  # max(nums[i] - nums[j]) for i < j
        for k in range(len(nums)):
            result = max(result, max_diff * nums[k])
            max_diff = max(max_diff, max_val - nums[k])
            max_val = max(max_val, nums[k])
        return result