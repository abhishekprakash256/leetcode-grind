"""
When a contiguous block of text is selected in a PDF viewer, the selection is highlighted with a 
blue rectangle. In this PDF viewer, each word is highlighted independently. For example:

"""

"""
approach -- 



keys = list("abcdefghijklmnopqrstuvwxyz")

values = h
mapper = dict(zip(keys, values))

#make rect area
max_height = 0 

for i in word:

	max_height = max(max_height,mapper[i])

return max_height * len(word)


"""

def designerPdfViewer(h, word):
	"""
	The function to make the area code
	code passes
	"""

	#make the dict
	keys = list("abcdefghijklmnopqrstuvwxyz")

	mapper = dict(zip(keys, h))

	#make the max height
	max_height = 0 

	#get the max height
	for char in word:

		max_height = max(max_height, mapper[char])

	#return the area
	return max_height * len(word)



 