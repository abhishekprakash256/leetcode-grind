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

	def helper_dfs(self,sequence):
		"""
		The function to make the dfs and find the seq
		"""

		#print(sequence)

		#base case 
		if len(sequence) > len(self.s) :

			return 

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




s = "leetcode"
wordDict = ["leet","code"]


sol = Solution()
print(sol.wordBreak(s,wordDict))











