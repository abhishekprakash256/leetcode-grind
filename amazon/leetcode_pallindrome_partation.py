"""
Given a string s, partition s such that every substring of the partition is a 
palindrome. Return all possible palindrome partitioning of s.
"""

"""

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]


Constraints:

1 <= s.length <= 16
s contains only lowercase English letters.
"""



"""
approach -- 

make all the combinatiosn and check if passes then append in the result list 


"""

from typing import List



class Solution_wrong:

    def __init__(self):

        self.results = []


    def _check_pallindrome(self,temp_str):
        """
        The function to check for the pallindrome
        """
        #constarint case 
        if len(temp_str) == 1 :

            return True

        #ptrs
        l , r = 0 , len(temp_str) - 1 

        while l <= r :

            if temp_str[l] != temp_str[r] :

                return False

            l +=1 
            r -= 1

        return True


    def _helper_dfs(self,idx,temp_str):
        """
        The function for the dfs search for the pallindrome 
        """

        #base case 

        if idx >= len(self.s) -  1:

            if self._check_pallindrome(temp_str) :

                self.results.append([temp_str])

                return


        #make the recursive calls
        for i in range(idx,len(self.s)) :

            temp_str += self.s[i]

            print(temp_str)

            if self._check_pallindrome(temp_str):

                self.results.append([temp_str])

            self._helper_dfs(idx + 1, temp_str)



    def partition(self, s: str) -> List[List[str]]:
        """
        The function to foound all the partation of the list that are pallindrome 
        """

        self.s = s 

        #constraint case 
        #if one length 
        if len(self.s) == 1 :

            return [[self.s]]

        #vars 
        temp_str = ""
        idx = 0

        #make the function call
        self._helper_dfs(idx,temp_str)

        return self.results




class Solution:
    def __init__(self):
        self.results = []

    def _check_palindrome(self, temp_str: str) -> bool:
        """Check if a given string is a palindrome."""
        return temp_str == temp_str[::-1]

    def _helper_dfs(self, idx: int, path: List[str]):
        """DFS function to find palindrome partitions."""
        if idx == len(self.s):
            self.results.append(path[:])  # Store a copy of the valid partition
            return

        for i in range(idx, len(self.s)):

            temp_str = self.s[idx:i + 1]  # Extract substring

            if self._check_palindrome(temp_str):
                path.append(temp_str)  # Choose
                self._helper_dfs(i + 1, path)  # Explore
                path.pop()  # Backtrack


    def partition(self, s: str) -> List[List[str]]:
        """Find all possible palindrome partitions of a string."""
        self.s = s
        self.results = []  # Reset results

        self._helper_dfs(0, [])  # Start DFS

        return self.results




class Solution:
    def __init__(self):
        self.results = []

    def _check_pallindrome(self,temp_str) :
        """
        The function to check for the pallindrome 
        """

        return temp_str == temp_str[::-1]


    def _helper_dfs(self,idx,path):
        """
        The function to check to do the dfs traversal 
        """

        #base case 
        if idx == len(self.s) :

            self.results.append(path)

            return

        #recursive calls 
        for i in range(idx,len(self.s)):

            temp_str = self.s[idx: i + 1]

            if self._check_pallindrome(temp_str) :

                self._helper_dfs(i + 1 ,path + [temp_str])



    def partition(self, s: str) -> List[List[str]]:
        """Find all possible palindrome partitions of a string."""
        self.s = s

        self._helper_dfs(0, [])  # Start DFS

        return self.results














sol = Solution()

s = "aab"


print(sol.partition(s))


