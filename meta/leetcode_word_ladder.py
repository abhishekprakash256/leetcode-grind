"""
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

    Every adjacent pair of words differs by a single letter.
    Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
    sk == endWord

Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.


"""

"""

Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.

Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.

 

Constraints:

1 <= beginWord.length <= 10
endWord.length == beginWord.length
1 <= wordList.length <= 5000
wordList[i].length == beginWord.length
beginWord, endWord, and wordList[i] consist of lowercase English letters.
beginWord != endWord
All the words in wordList are unique.



"""



"""
approach  -- 

make a adjacnency list graph 

using the special character 

then add the remaing word in the list 






"""

from typing import List

from collections import deque, defaultdict


class Solution():
	"""
	passses leetcode
	"""

	def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
		"""
		The function to find the length of the words
		"""

		#constarint case 
		if endWord not in wordList :
			return 0

		#the word mapper 
		mapper = defaultdict(list)	

		wordList.append(beginWord)

		#make the graph 
		for word in wordList :

			for j in range(len(word)):

				pattern = word[:j] + "*" + word[j+1:]

				mapper[pattern].append(word)

		#make the visit set 
		visited = set([beginWord])

		#make the queue 
		queue = deque([beginWord])

		#result 
		result = 1 

		#start the bfs traversal 
		while queue :
			
			#make the iter for the queue
			for i in range(len(queue)):

				word = queue.popleft()
			
				if word == endWord :

					return result

				for j in range(len(word)) :

					pattern = word[:j] + "*" + word[j+1:]

					for neighbor in mapper[pattern] :

						if neighbor not in visited :

							visited.add(neighbor)

							queue.append(neighbor)

			result +=1 

		return 0





class Solution_optim:
	"""
	passes leetcode
	"""
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        Find the shortest transformation sequence from beginWord to endWord
        using words in wordList, changing one letter at a time.
        """

        # Constraint check
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0

        # Create adjacency list (pattern -> words)
        mapper = defaultdict(set)
        wordSet.add(beginWord)  # Ensure beginWord is included

        for word in wordSet:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                mapper[pattern].add(word)

        # BFS Initialization
        queue = deque([beginWord])
        visited = set([beginWord])
        result = 1  # The transformation count starts at 1

        # BFS traversal
        while queue:
            for _ in range(len(queue)):  # Level-wise iteration
                word = queue.popleft()

                if word == endWord:
                    return result

                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]

                    for neighbor in mapper[pattern]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)

            result += 1  # Increment step count

        return 0  # If no path is found










beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]







sol = Solution()

print(sol.ladderLength(beginWord, endWord, wordList))







