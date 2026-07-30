from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template('index.html')

@app.route('/post')
def post_page():
    return render_template('post.html')

@app.route('/post2')
def post2_page():
    return render_template('post2.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)