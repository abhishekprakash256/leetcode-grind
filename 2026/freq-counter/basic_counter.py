"""
basic freuq counter
"""


from collections import Counter

def freq_counter(nums) :

	mapper = {}

	for i in nums :

		if i in mapper :

			mapper[i] = mapper[i] + 1 

			continue

		mapper[i] = 1

	return mapper





def freq_counter_2(nums):

	freq = Counter(nums)

	return freq



nums = [1,1,2,3,2,1]

res = freq_counter(nums)

res2 = freq_counter_2(nums)

print(res)

print(res2)