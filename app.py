#!/usr/bin/env python

from flask import Flask, render_template,request,url_for,redirect
from flask_wtf import Form
from wtforms.fields import RadioField, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!' #protect against csrf protection
guesses = ['Python','Ruby','Node.JS']
questions = ['Is it complied???','Does it run on VM???']

#code for creating the form
class YesNoQuestionForm(Form):
    answer = RadioField('Your answer',choices=[('yes','Yes'),('no','No')])
    submit = SubmitField('Submit')

@app.route('/')
def index():
    print 'name'+__name__
    return render_template('index.html')

#we have to tell the route that to handle the POST request
@app.route('/question/<int:id>',methods=['GET','POST'])
def question(id):
    form = YesNoQuestionForm()
    #the function is gonna check
    if form.validate_on_submit():
        if form.answer.data == 'yes':
            return redirect(url_for('question',id = id+1))
        else:
            return redirect(url_for('question',id=id))
    # print request
    # if request.method == 'POST':
    #     if request.form['answer'] == 'yes':
    #         return redirect(url_for('question',id = id+1))
    #     else:
    #         return redirect(url_for('question',id = id))
    return render_template('question.html',question = questions[id],form = form)

@app.route('/guess/<int:id>')
def guess(id):
    return render_template('guess.html',guess = guesses[id])

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
