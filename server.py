from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'Highway_to_the_danger_zone'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result')
def user():
    return render_template('user.html')

@app.route('/submit_survey',methods=['POST'])
def surveyed():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    print(session)
    return redirect('/result')

if __name__=='__main__':
    app.run(debug=True)