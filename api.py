from flask import Flask, render_template, request, jsonify, session, flash, redirect
from flask_session import Session
from editdistancespellcheck import known, oneEditDist
from makeSuggestions import *

app = Flask(__name__, template_folder="templates")
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route("/lang" , methods=['GET', 'POST'])
def test():
    if request.method == 'POST':
        select = request.form.get('ui_language')
        if(select == 'Irish'):
            return render_template('Irish.html')
        if(select == 'English'):
            return render_template('SpellC.html')



@app.route('/', methods = ['GET','POST'])
def my_form_post():
	if request.method == "POST":
		if request.form["submit_button"] == "submit":
			session['text'] = request.form.get("text")
			session['given_text'] = session['text']

			#session['words'] = session['text'].split()
			session['misspelled'] = []

			bad = getMisspelled(session['text'])
			for word in bad:
				session['misspelled'].append(word)
			session['suggestions'] = dict.fromkeys(session['misspelled'])
			for key in session['suggestions']:
				for i in range(len(makeSuggestions(key))):
					session['suggestions'][key] = makeSuggestions(key)[i]
			return render_template("/SpellC.html", text=session['given_text'], misspelled=session['misspelled'], suggestions=session['suggestions'])

		if request.form["submit_button"] == "correct":
			session['new_text'] = session['given_text']
			for word in session['misspelled']:
				if request.form.get(word) != None:
					session['new_text'] = session['new_text'].replace(word, request.form.get(word))
				else:
					error = "Please choose a correction for all misspelled words."
			return render_template("/SpellC.html", error=error, text=session['given_text'], new_text=session['new_text'], misspelled=session['misspelled'], suggestions=session['suggestions'])



	else:
		return render_template("/SpellC.html")


if __name__=='__main__':
	app.run(debug=True, host='0.0.0.0', port=5000)


