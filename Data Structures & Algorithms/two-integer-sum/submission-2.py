class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = dict()
        for index, value in enumerate(nums):
            key = target - value
            if key in lookup:
                ans = [index, lookup[key]]
                ans.sort()
                return ans

            lookup[value] = index
        
        return [-1, -1]