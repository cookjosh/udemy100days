from flask import Flask, render_template
import requests
app = Flask(__name__)

response = requests.get('https://api.npoint.io/6aeb592b24ad9ad9d835')
data = response.json()

@app.route('/')
def home():
    return render_template('index.html', data=data)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/post/<int:index>')
def post(index):
    requested_post = None
    for post in data:
        if post['id'] == index:
            requested_post = post
    return render_template('post.html', post=requested_post)




if __name__ == '__main__':
   app.run(debug=True)