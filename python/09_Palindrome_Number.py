# time: o(n)
# space: o(1)

class Solution:
    def isPalindrome(self, x: int) -> bool:
        int_to_str = str(x)

        return int_to_str == int_to_str[::-1]
