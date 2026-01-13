class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = []
        longest = 0

        for i in range(len(s)):
            if s[i] not in substring:
                substring.append(s[i])
            else:
                if len(substring) > longest:
                    longest = len(substring)
                substring = [s[i]]

        if longest == 0 and len(s) != 0:
            return 1 
        return longest
