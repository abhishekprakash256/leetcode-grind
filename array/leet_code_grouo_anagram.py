"""
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.
"""

strs = ["eat","tea","tan","ate","nat","bat"]
out = [["bat"],["nat","tan"],["ate","eat","tea"]]


"""
approach 

sort each of elemnet and compare and put in the hashmap as keys and the index as the values of each element 

"""



class Solution(object):
	def groupAnagrams(self, strs):
		"""
		:type strs: List[str]
		:rtype: List[List[str]]
		"""
		
		#make hash map 

		mapper = {}

		for i in range(len(strs)):

			sorted_strs = sorted(strs[i])

			sorted_strs = ''.join(sorted_strs)

			if sorted_strs in mapper:

				mapper[sorted_strs].append(strs[i])

			else:
				val_lst = [strs[i]]
				mapper[sorted_strs] = val_lst


		for key in mapper:
			mapper[key] = mapper[key]

		return list(mapper.values())   





if __name__ == "__main__":

	sol = Solution()

	res = sol.groupAnagrams(strs)

	print(res)