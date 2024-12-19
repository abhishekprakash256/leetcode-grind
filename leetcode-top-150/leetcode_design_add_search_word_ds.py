"""
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
 
"""

"""

Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]

Output

[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True

"""

"""
approach --- 

waht about a trie ? 

what abot the ".." matching ?  


class TrieNode:

	def __init__(self):
		self.children = {}
		self.end = False


class WordDictionary:

	def __init__(self):
		self.root = TrieNode() 



	def addWord(self,word) :

		node = self.root 

		for char in word :

			if char not in self.children :

				self.children[char] = TrieNode()

			node = node.children[char]

		node.end = True


	def search(self,word):

		node = self.root

		for char in word :

			if char != "." :

				if char not in self.children:
					return False

			node = node.children[char]

		return True
		



"""

class TrieNode:
	"""
	Wrong code 
	"""

	def __init__(self):
		self.children = {}
		self.end = False


class WordDictionary:

	def __init__(self):
		self.root = TrieNode() 


	def addWord(self,word) :

		node = self.root 

		for char in word :

			if char not in node.children :

				node.children[char] = TrieNode()

			node = node.children[char]

		node.end = True


	def search(self,word):

		node = self.root

		for char in word :

			if char != "." :

				if char not in node.children:
					return False

			node = node.children[char]

		return True















class TrieNode:
	"""
	Passes leet code 

	"""
    def __init__(self):
        self.children = {}
        self.end = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """
        Adds a word to the dictionary.
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.end = True

    def search(self, word: str) -> bool:
        """
        Searches for a word in the dictionary, supporting the '.' wildcard.
        """
        def dfs(node: TrieNode, i: int) -> bool:
            if i == len(word):  # Base case: fully traversed the word
                return node.end

            char = word[i]
            if char == ".":
                # Check all possible paths for the wildcard
                for child in node.children.values():
                    if dfs(child, i + 1):
                        return True
                return False
            else:
                # Regular character case
                if char not in node.children:
                    return False
                return dfs(node.children[char], i + 1)

        return dfs(self.root, 0)

