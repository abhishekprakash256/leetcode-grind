"""
iven a string s, rearrange the characters of s so that any two adjacent characters are not the same.

Return any possible rearrangement of s or return "" if not possible.
"""


"""
Example 1:

Input: s = "aab"
Output: "aba"

Example 2:

Input: s = "aaab"
Output: ""

 

Constraints:

1 <= s.length <= 500
s consists of lowercase English letters.


"""


"""
approach -- 


making a dfs search - 

with cond of elemnt not equal 

the length has to be same 

start the iter with same idx


return if 

else return ""

"""





from collections import Counter

class Solution_slow:
    def helper_dfs(self, temp_str):
        """
        The function to construct the string where no adjacent characters are the same.
        """

        # Base case: If the string is fully built, return it
        if len(temp_str) == len(self.s):
            return temp_str

        # Try adding each character to the current string
        for i in range(len(self.s)):
            # Ensure the last character is not the same as the current one and it is not used
            if not self.used[i] and (not temp_str or temp_str[-1] != self.s[i]):
                self.used[i] = True  # Mark as used
                res = self.helper_dfs(temp_str + self.s[i])
                if res:  # If a valid solution is found, return it immediately
                    return res
                self.used[i] = False  # Backtrack and restore

        return False  # No valid arrangement found

    def reorganizeString(self, s: str) -> str:
        """
        Function to reorganize the string so that adjacent characters are not the same.
        """

        self.s = s
        self.used = [False] * len(s)  # Keep track of used characters
        
        # Constraint: If any character appears more than (N+1)/2 times, it's impossible
        freq = Counter(s)
        if max(freq.values()) > (len(s) + 1) // 2:
            return ""

        # Start DFS search
        return self.helper_dfs("") or ""





class Solution:
    def reorganizeString(self, s: str) -> str:
        ans = []
        # Min heap ordered by character counts, so we will use
        # negative values for count
        pq = [(-count, char) for char, count in Counter(s).items()]
        heapify(pq)

        while pq:

            count_first, char_first = heappop(pq)

            if not ans or char_first != ans[-1]:

                ans.append(char_first)
                if count_first + 1 != 0: 
                    heappush(pq, (count_first + 1, char_first))

            else:
                
                if not pq: return ''

                count_second, char_second = heappop(pq)

                ans.append(char_second)

                if count_second + 1 != 0:

                    heappush(pq, (count_second + 1, char_second))

                heappush(pq, (count_first, char_first))


        return ''.join(ans)









s = "aab"

      
sol = Solution()

print(sol.reorganizeString(s))


























