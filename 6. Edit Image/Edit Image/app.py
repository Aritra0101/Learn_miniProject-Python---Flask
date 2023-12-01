import os
from flask import Flask, flash, request, redirect, url_for, render_template, request
from werkzeug.utils import secure_filename
import cv2

UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}

app = Flask(__name__)
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def processImage(filename, operation):
    img = cv2.imread(f"uploads/{filename}")
    if operation == "cPNG":
        newFileName = f"{filename.split('.')[0]}.png"
        cv2.imwrite(f"static/{newFileName}", img)
        return newFileName
    elif operation == "cWEBP":
        newFileName = f"{filename.split('.')[0]}.webp"
        cv2.imwrite(f"static/{newFileName}", img)
        return newFileName
    elif operation == "cJPG":
        newFileName = f"{filename.split('.')[0]}.jpg"
        cv2.imwrite(f"static/{newFileName}", img)
        return newFileName
    elif operation == "cGREY":
        imgProcessed = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.imwrite(f"static/{filename}", imgProcessed)
        return filename

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/price')
def price():
    return render_template('price.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/edit', methods=['GET', 'POST'])
def edit():
    if request.method == 'POST':
        operation = request.form.get("operation")
        print(operation)
        if operation == 'Choose an Operation':
            return "No Operation Found. Please try again"
        if 'file' not in request.files:
            flash('No file part')
            return "No Input File Found. Please try again"
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return "No Input File Found. Please try again"
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            newFileName = processImage(filename, operation)
            flash(f"Your Image is processed and available <a href='/static/{newFileName}' target='_black'> here </a>")
            return render_template('index.html')
    else:
        return "GET"

app.run(debug=True, port=5000)