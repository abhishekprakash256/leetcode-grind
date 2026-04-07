"""
basic freuq counter
"""



def freq_counter(nums) :

	mapper = {}

	for i in nums :

		if i in mapper :

			mapper[i] = mapper[i] + 1 

			continue

		mapper[i] = 1

	return mapper




nums = [1,1,2,3,2,1]

res = freq_counter(nums)

print(res)