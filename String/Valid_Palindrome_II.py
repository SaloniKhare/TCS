class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(left: int, right: int) -> bool:
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        i, j = 0, len(s) - 1
        
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                # If a mismatch occurs, try skipping s[i] OR skipping s[j]
                return is_palindrome(i + 1, j) or is_palindrome(i, j - 1)
                
        return True



class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        l, r = 0, n - 1
        while l < r:
            if s[l] != s[r]:
                sl = s[:l] + s[l + 1:]
                sr = s[:r] + s[r + 1:]
                if sl == sl[:][::-1] or sr == sr[:][::-1]:
                    return True
                else:
                    return False
            else:
                l += 1
                r -= 1
        return True

        
