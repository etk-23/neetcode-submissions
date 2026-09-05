class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return n

        ptr1, ptr2 = 0, 1
        ans = 1

        while ptr2 < n:
            if s[ptr2] in s[ptr1 : ptr2]:
                ans = max(ans, len(s[ptr1 : ptr2]))
                ptr1 = s.index(s[ptr2], ptr1, ptr2) + 1
            ptr2 += 1
        
        ans = max(ans, len(s[ptr1 : ptr2]))
        return ans