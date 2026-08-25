class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ''
        for word in strs:
            ans += word
            ans += '#!'
        return ans
    def decode(self, s: str) -> List[str]:
        ans = []
        word = ''
        n = len(s)
        i = 0

        while i < n:
            if s[i] == '#':
                if i+1 < n and s[i+1] == '!':
                    ans.append(word)
                    word = ''
                    i += 1
                else:
                    word += s[i]
            else:
                word += s[i]
            i += 1
        print(word, '1')
        if word:
            ans.append(word)
        return ans