class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        ans = 1
        count = 1
        nums.sort()

        for i in range(1, n):
            if nums[i] == nums[i-1]:
                continue
            if nums[i] == nums[i-1] + 1:
                count += 1
            else:
                count = 1
            ans = max(ans, count)

        return ans