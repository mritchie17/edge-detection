import os

from flask import Flask, flash, render_template, redirect, request

UPLOAD_FOLDER = '/static/uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

def create_app():
	# create and configure the app
	app = Flask(__name__, instance_relative_config=True)
	app.config['SECRET_KEY'] = 'REPLACE_WITH_RANDOM'
	app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

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
	if 'file' not in request.files:
		flash('No file part')
		return redirect(request.url)
	file = request.files['file']
	if file.filename == '':
		flash('No selected file')
		return redirect(request.url)
	if file and allowed_file(file.filename):
		filename = secure_filename(file.filename)
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		return render_template('display.html', filename=filename)
	else:
		flash("Not an allowed image type.  Allowed types are txt, pdf, png, jpg, jpeg.")
		return redirect(request.url)
	return "hiya"

@app.route('/')
def form():
	return render_template('form.html')
