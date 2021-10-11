from flask import Flask, render_template, request, jsonify
from editdistancespellcheck import known, oneEditDist
from makeSuggestions import *

app = Flask(__name__)

#def get_text(text):
#	text = text.lower()
#	return text

@app.route('/')
def home():
	return render_template('SpellC.html')

#@app.route('/join', methods=['GET', 'POST'])
#def my_form_post():
#	text = request.form['text']
#	word = request.args.get('text')
#	text = get_text(text)
#	result = {
#		"output": text
#	}
#	result = {str(key): value for key, value in result.items()}
#	return jsonify(result=result)

#@app.route('/', methods = ['POST'])
#def my_form_post():
#	text = request.form['text']
#	processed_text = text.upper()
#	return processed_text

@app.route('/', methods = ['POST'])
def my_form_post():
	text = request.form['text']
	#text = text.lower()
	#print(text)
	#text = text.split(" ")
	#newText = []
	#for i in text:
	#	ans = known(oneEditDist(i))
	#	newText.append(ans[0])
	#newText = " ".join(newText)
	#return newText
	return makeSuggestions(text)

if __name__=='__main__':
	app.run(debug=True, host='0.0.0.0', port=5000)
