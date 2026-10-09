class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        palindrome=""

        for i in s:
            if i.isalnum():
                palindrome +=i
            
        return palindrome==palindrome[::-1]