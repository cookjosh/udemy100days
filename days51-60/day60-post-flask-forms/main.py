from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home():
    return render_template('index.html')

# Solution I came up with is different than course solution!
@app.route('/login', methods = ['POST'])
def receive_login():
    username = request.form.get('username')
    password = request.form.get('password')
    data = {
        'username': username,
        'password': password,
    }
    return render_template('login.html', data = data)




if __name__ == '__main__':
   app.run(debug=True)