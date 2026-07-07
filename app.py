#the code is taken from one of remote repo
# Doing test 3 for linter
#Doing a Deliberate syntax error in code to check the linter working through ZGithub Action 

import os  # Deliberate mistake: unused import, Ruff should catch this
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')

Adding a secuity check {
    def Sec Harshit_error


@app.route('/health')
def health():
    return 'Server is up and running'
