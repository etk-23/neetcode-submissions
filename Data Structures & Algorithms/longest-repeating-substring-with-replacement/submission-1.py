class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        ans = 0
        chars = {}

        l = 0
        count = 0
        for r in range(n):
            chars[s[r]] = chars.get(s[r], 0) + 1
            count = max(count, chars[s[r]])

            while (r - l + 1) - count > k:
                chars[s[l]] -= 1
                l += 1

            ans = max(ans, (r - l + 1))
        
        return ans