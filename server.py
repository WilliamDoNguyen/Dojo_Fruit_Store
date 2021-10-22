from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'super secret key. none shall pass'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])
def process_checkout():
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['email'] = request.form['student_id']
    session['strawberry'] = request.form['strawberry']
    session['raspberry'] = request.form['raspberry']
    session['apple'] = request.form['apple']
    return redirect('/checkout')

@app.route('/checkout')
def show_checkout():
    return render_template("checkout.html", first_name = session['first_name'], last_name = session['last_name'], email=session['email'], Customer_name = session['first_name'], Strawberry = session['strawberry'], Raspberry = session['raspberry'], Apple = session['apple'], count = int(session['strawberry']) + int(session['raspberry']) + int(session['apple']))

@app.route('/fruits')
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":
    app.run(debug=True)
