import os

from flask import Flask, render_template, request


def create_app():
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    return app

app = create_app()

@app.route('/hello')
def hello():
	return 'Hello, World!'

@app.route('/process', methods=['POST'])
def process_form():
	#lol do stuff later
	return "hiya"

@app.route('/')
def form():
	return render_template('form.html')
