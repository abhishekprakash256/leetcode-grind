"""
Given a string s, return the longest 
palindromic
 
substring
 in s.

"""

"""

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"

babbbab

sliding window ? from left ? 

brute force use two pointer 

start from middle ? 

expand issues ? 



"""

"""
approach -- 

using sliding window 

make a function for checking the pallindrome 

and remove elemnet taht is not 

baaabbbbbc - > 


"""



class Solution_brute_force():
    """
    The brute force solution is slow 
    """
    def _is_palindrome(self, s, i, j):
        """
        Check if the substring s[i:j+1] is a palindrome.
        """
        left, right = i, j

        while left <= right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    def longestPalindrome(self, s: str) -> str:
        """
        Brute force approach for longest palindromic substring.
        """
        if not s:
            return ""

        if len(s) == 1:
            return s

        result = s[0]
        max_length = 1  # At least one character is always a palindrome.

        for i in range(len(s)):
            for j in range(i, len(s)):  # Include j=i to check single character cases
                if self._is_palindrome(s, i, j):
                    if (j - i + 1) > max_length:  # Correct length check
                        max_length = j - i + 1
                        result = s[i:j+1]

        return result







class Solution:
    def _expand_center(self, i, j):
        """
        Expands around the center and returns the length of the longest palindrome.
        """
        while i >= 0 and j <= len(self.s) - 1 and self.s[i] == self.s[j]:  # Order of conditions fixed
            i -= 1
            j += 1
        return j - i - 1  # Length of palindrome

    def longestPalindrome(self, s: str) -> str:
        """
        Expand around center approach for longest palindromic substring.
        """
        if not s:
            return ""
        
        self.s = s
        start, end = 0, 0  # Stores the indexes of the longest palindrome

        for i in range(len(s)):
            odd = self._expand_center(i, i)      # Odd-length palindrome
            even = self._expand_center(i, i+1)  # Even-length palindrome
            
            max_length = max(odd, even)

            if max_length > (end - start):  # Update result if a longer palindrome is found
                start = i - (max_length - 1) // 2
                end = i + max_length // 2

        return s[start:end+1]  # Return the longest palindromic substring


