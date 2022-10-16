
from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)
app.config['SECRET_KEY'] = 'super secret key'


@app.route("/")
@app.route('/register', methods=['GET'])
def Newregister():
    return render_template('Register.html', title="Register")


@app.route("/register/<message>", methods=['GET'])
def register(message):
    if message:
        return render_template('Register.html', title="Register", message=message)


@app.route("/display", methods=['POST'])
def display():
    if(request.method == 'POST'):
        if(request.form['password'] != request.form['ConfirmPassword']):
            return redirect(url_for('register', message='Password does not match'))
        else:
            details = {
                'name': request.form['name'], 'email': request.form['email'], 'phoneNumber': request.form['phoneNumber'], 'password': request.form['password']}
            return render_template('Display.html', title="Display", RegisteredDetails=details)


if __name__ == "__main__":
    app.run(debug=True)
