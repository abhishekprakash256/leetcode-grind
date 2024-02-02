"""
group the anagram strings together 
"""

strs = ["eat","tea","tan","ate","nat","bat"]
out = [["bat"],["nat","tan"],["ate","eat","tea"]]

strs2 = [""]
out2 = [""]

strs3 = ["a"]
out3 = ["a"]


"""
algo --

sort the string use as key for hash map 

add the next in the list as per key found 

return key values append in the list as per iteration 

"""


class Solution:
	def groupAnagrams(self, strs):
		"""
		The function to find the group anagram of strings 
		"""
		#hash map to map values 
		mapper = {}
		anagram_lst = []
		for val in strs:

			val_str = "".join(sorted(val))

			if val_str not in mapper:
				mapper[val_str] = [val]

			else:
				mapper[val_str].append(val)

		
		return [mapper.values()]


sol = Solution()
res = sol.groupAnagrams(strs)

print(res)

		