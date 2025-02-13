"""
Given an input string s and a pattern p, implement regular expression matching 
with support for '.' and '*' where:

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

 
"""

"""

Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
 

Constraints:

1 <= s.length <= 20
1 <= p.length <= 20
s contains only lowercase English letters.
p contains only lowercase English letters, '.', and '*'.
It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.

"""

"""
approach -- 

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

s = "aa"

p = "a"

for char in p :

	if char == "*":

		return True

	if char == "." :



"""


class Solution:
	"""
	passes leetcode
	"""
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        
        # DP table with (m+1) x (n+1) size, initialized to False
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        
        # Base Case: Empty string matches empty pattern
        dp[0][0] = True  

        # Fill for patterns with '*' that can match empty string
        for j in range(2, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == s[i - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]  # Match previous character
                
                elif p[j - 1] == '*':
                    # Ignore '*' and preceding character (zero occurrence) -> dp[i][j-2]
                    dp[i][j] = dp[i][j - 2]
                    
                    # If preceding character matches current character in `s`, or it is '.'
                    if p[j - 2] == s[i - 1] or p[j - 2] == '.':
                        dp[i][j] = dp[i][j] or dp[i - 1][j]  # Use '*' to match multiple chars
        
        return dp[m][n]  # Final result at the last cell
