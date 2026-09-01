class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l, r = 0, n-1
        ans = 0

        while l < r:
            # area = length * height
            curr = (r - l) * min(heights[l], heights[r])
            print(curr)
            ans = max(ans, curr)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return ans