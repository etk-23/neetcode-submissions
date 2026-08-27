# SOLUTION = PREFIX + SUFFIX
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n
        prefix = [0] * n
        suffix = [0] * n

        prefix[0] = suffix[n-1] = 1
        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1]
            suffix[n-1-i] = suffix[n-i] * nums[n-i]
            ans[i] *= prefix[i]
            ans[n-1-i] *= suffix[n-1-i]

        #print(prefix, suffix)
        return ans