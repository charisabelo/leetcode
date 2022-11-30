# time: n * m
# space: o(n)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = 0
        max_len = 0
        curr_substr = ''

        while end < len(s):
            if s[end] not in curr_substr:
                curr_substr += s[end]
            elif s[end] in curr_substr:
                max_len = max(max_len, len(curr_substr))
                curr_substr = ''
                start += 1
                end = start
                continue

            end += 1

        return max(max_len, len(curr_substr))
