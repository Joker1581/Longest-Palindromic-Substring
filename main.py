class Solution:
    def expand(s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return [left + 1, right]
    def longestPalindrome(self, s: str) -> str:
        cur_p = (0, 1)
        for i in range(1, len(s)):
            odd_p = self.expand(s, i-1, i+1)
            even_p = self.expand(s, i-1, i)
            longest_p = max(odd_p, even_p, key=lambda x: x[1] - x[0])
            cur_p = max(longest_p, cur_p, key=lambda x: x[1] - x[0])
        return s[cur_p[0]: cur_p[1]]
        
if __name__ == "__main__":
    print(Solution.longestPalindrome(Solution, "babad"))