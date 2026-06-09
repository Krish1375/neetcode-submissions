class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        max_length = 0
        res_set = set(nums)

        for i in range(len(nums)):
            if nums[i] - 1 not in res_set:
                curr = nums[i]
                temp_length = 1
                while curr + 1 in res_set:
                    curr+=1
                    temp_length+=1
                max_length = max(max_length, temp_length)
        return max_length
    