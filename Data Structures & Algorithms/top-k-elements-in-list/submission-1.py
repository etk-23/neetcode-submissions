class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans = []

        d = {}

        for i in range(n):
            d[nums[i]] = d.get(nums[i], 0) + 1

        d_sorted = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
        #print(d_sorted)
        d_list = list(d_sorted.keys())
        #print(d_list)
        return d_list[0:k]
