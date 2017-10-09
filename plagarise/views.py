from flask import Flask, render_template, request, session
import webai as a
import textsurm as summarise
import plotstuff as plot

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def startdis():
  return render_template("base.html")



@app.route('/generate', methods=['POST'])
def runai():
    question = request.form['entertext']
    theanswer= a.rundis(question)
    iterations = plot.check_iterations()
    progress = (iterations /5000) * 100

    return render_template("main.html",theanswer=theanswer)

@app.route('/summarise', methods=['POST'])
def runaitwo():
    question = request.form['entertextsum']
    thesummarised=summarise.FrequencySummariser().summarize(question,2)


    return render_template("maintwo.html",thesummarised=thesummarised)



