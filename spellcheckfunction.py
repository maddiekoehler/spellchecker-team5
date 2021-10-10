def spellcheck(text, dict):
	"""identify misspelled words and correct input text
		:return suggestion and some measure of similarity with input text (for ranking suggestions)
	"""

	#define dictionary once that is figured out

	suggestion = []
	suggestion_similarity = []
	replaced_terms = 0

	#remove punctuation
	text = text.translate(str.maketrans('', '', string.punctuation))

	for token in text.split():
	#if word is mispelled
	if not d.check(token):
		new_token = d.suggest(token)[0]
		suggestion.append(new_token)
		#calculate similarity
		suggestion_similarity.append(similarity)
	else:
		suggestion.append(token)
		suggestion_similarity.append(1) #word identical


	return suggested_text, overall_similarity
