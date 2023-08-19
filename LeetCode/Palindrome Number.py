class Solution:
    def isPalindrome(x: int) -> bool:
        if x < 0:
            return False
        else:
            reverse = str(x)[::-1]
            if str(x) == reverse:
                return True
            else:
                return False
            
print(Solution.isPalindrome(-121))
print(Solution.isPalindrome(121))