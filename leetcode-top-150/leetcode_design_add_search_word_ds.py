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
