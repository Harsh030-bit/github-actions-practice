#the code is taken from one of remote repo
# Doing test 3 for linter
#Doing a Deliberate syntax error in code to check the linter working through ZGithub Action 


from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/health')
def health():
    return 'Server is up and running'
