from flask import Flask, render_template, request, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mykey'

app.debug = True

debug = DebugToolbarExtension(app)
DEBUG_TB_INTERCEPT_REDIRECTS = False
responses =[]

@app.route('/')
def get_root():
    survey = satisfaction_survey.title
    instrucs = satisfaction_survey.instructions
    questions = satisfaction_survey.questions
    return render_template('/home.html', survey = survey, instrucs = instrucs, questions = questions)

@app.route('/complete')
def fin():
    return render_template("survey_complete.html", responses = responses)


@app.route('/questions/<int:question>')
def get_questions(question):
    length = len(satisfaction_survey.questions)
    answered = len(responses)
    if question == answered:
        if question < length:
            return render_template("questions.html", question=question,
            question_text = satisfaction_survey.questions[question].question,
            question_ans = satisfaction_survey.questions[question].choices,
            )
        else:
            return redirect('/complete')
    else:
        flash("Please answer this question")
        return redirect(f'/questions/{answered}')


@app.route('/answers/<int:question>', methods=["POST"])
def post_answer(question):
    if request.form.get("answer"):
        answer = request.form.get("answer")
        responses.append(answer)
    question = question

    return redirect(f'/questions/{question + 1}')


