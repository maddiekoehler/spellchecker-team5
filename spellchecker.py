class SpellChecker:
	"""SpellChecker class
		-suggestion [string]: recommended sentence
		-similarity [double]: similarity between input and recommendation
	"""

	def __init__(self, suggestion, similarity):
		self.suggestion = suggestion
		self.similarity = similarity
