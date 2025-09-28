from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():

    context_data = {
        'title': 'Flask with Jinja',
        'user_name': 'Vishwas'
    }

    return render_template('index.html', **context_data)

if __name__ == '__main__':
    app.run(debug=True)