class Solution:
    def isPalindrome(self, s: str) -> bool:
        #create pointers
        l , r = 0, len(s) - 1

        #increment the left and decrement the right
        while l < r:
            #until the left pointer reaches the right pointer,
            while l < r and not self.isAlphaNum(s[l]):
                l += 1
            while r > l and not self.isAlphaNum(s[r]):
                r -= 1
            #check while left and right pointers for alphanumeric
            if s[l].lower() != s[r].lower():
                return False

            l, r = l + 1, r - 1
        
        return True

    def isAlphaNum(self, c):
        return (
            ord('A') <= ord(c) <= ord('Z') or
            ord('a') <= ord(c) <= ord('z') or
            ord('0') <= ord(c) <= ord('9')
        )