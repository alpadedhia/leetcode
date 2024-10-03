import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub('[^0-9a-zA-Z]+', '', s).lower()
        left = 0
        right = len(s) - 1
        while left < right:
            if left == right:
                return True

            if s[left] != s[right]:
                return False

            left += 1
            right -= 1

        return True

            
        