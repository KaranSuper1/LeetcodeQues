
# Solution
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        if (x[::-1]==x):
            return "true"

# Test
y=Solution()
print(y.isPalindrome(121))