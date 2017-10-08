from flask import Flask, render_template, request, session
import webai as a
import textlit as lit
import plotstuff as plot

app = Flask(__name__)


@app.route('/')
def startdis():
  return render_template("base.html")



@app.route('/generate', methods=['POST'])
def runai():
    question = request.form['entertext']
    # file = request.form['enterfile']
    # if question.endswith(".txt") or file.endswith(".txt"):
    #     theanswer = lit.rundis(file)
    #     iterations = plot.check_iterationsfile(file)
    #     progress = (iterations / 10000) * 100
    # else:
    theanswer= a.rundis(question)
    iterations = plot.check_iterations()
    progress = (iterations /5000) * 100

    return render_template("main.html",theanswer=theanswer)



app.run(debug=True)
