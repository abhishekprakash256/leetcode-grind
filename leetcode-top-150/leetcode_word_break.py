"""

Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a 

space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.
"""



"""

Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false

 

Constraints:

1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.

"""

"""
approach using recursion -- 

#base case 
if len(word) > len(s) :
	
	return 

if word == s :

	return True


for word in WordDict:

	self.helper(+word)


"""



class Solution_slow():
	"""
	The solution is slow
	can't pass leetcode
	"""

	def helper_dfs(self,sequence):
		"""
		The function to make the dfs and find the seq
		"""

		#print(sequence)

		#base case 
		if len(sequence) > len(self.s) :

			return 

		# Check if sequence is a valid prefix of s.
		if not self.s.startswith(sequence):
			return False

		if sequence == self.s :

			return True

		#make the recursive call
		for word in self.wordDict :

			if self.helper_dfs(sequence + word) :

				return True

		return False




	def wordBreak(self,s,wordDict):
		"""
		The function to find the word in the dict
		"""

		self.wordDict = wordDict
		self.s = s

		#constraints 
		if len(self.wordDict) == 1 :

			if self.wordDict[0] == s :

				return True

			else:

				return False


		#make the recursive call

		return self.helper_dfs("")





class Solution_slow2():
	"""
	The solution is slow
	passes leetcode
	"""

	def __init__(self):

		self.memo = {}

	def helper_dfs(self,sequence):
		"""
		The function to make the dfs and find the seq
		"""

		#print(sequence)

		#base case 
		if len(sequence) > len(self.s) :

			return 

		#check in the memo
		if sequence in self.memo:

			return self.memo[sequence]


		if sequence == self.s :

			return True

		#make the recursive call
		for word in self.wordDict :

			if self.s.startswith(sequence) :

				if self.helper_dfs(sequence + word) :

					self.memo[sequence] = True

					return True

		self.memo[sequence] = False

		return False


	def wordBreak(self,s,wordDict):
		"""
		The function to find the word in the dict
		"""

		self.wordDict = wordDict
		self.s = s

		#constraints 
		if len(self.wordDict) == 1 :

			if self.wordDict[0] == s :

				return True

			else:

				return False


		#make the recursive call

		return self.helper_dfs("")




class Solution:
    def __init__(self):
        self.memo = {}

    def helper_dfs(self, start):
        """
        The function to make the DFS and find the sequence using index-based memoization.
        passes leetcode
        """
        # Base case: If we reach the end of the string, return True.
        if start == len(self.s):
            return True

        # Check in memo to avoid redundant computation.
        if start in self.memo:
            return self.memo[start]

        # Try every word in wordDict as a potential prefix starting from 'start'.
        for word in self.wordDict:
            if self.s.startswith(word, start):  # Check if `word` matches the substring starting at `start`.
                if self.helper_dfs(start + len(word)):  # Move to the next part of the string.
                    self.memo[start] = True
                    return True

        # If no valid word break is found, store False in the memo.
        self.memo[start] = False
        return False

    def wordBreak(self, s, wordDict):
        """
        The function to determine if the word can be segmented using wordDict.
        """
        self.s = s
        self.wordDict = set(wordDict)  # Convert to set for O(1) lookups.
        self.memo = {}  # Reset memo for a fresh computation.
        return self.helper_dfs(0)  # Start DFS from the beginning of the string.


s = "leetcode"
wordDict = ["leet","code"]


sol = Solution()
print(sol.wordBreak(s,wordDict))











