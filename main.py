import file_object
from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'


def upload_file(file_path):
    return file_object.FileClass(file_path)


@app.route('/')
def home():
    return render_template('my_app.html')


@app.route('/upload', methods=['POST'])
def upload_file_self():
    file_path = request.files['file'].filename
    print(file_path)
    F1 = upload_file(file_path)
    return redirect(url_for('my_app', file_name=F1.file_name))


@app.route('/view/<filename>')
def view_file(filename):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    try:
        with open(file_path, 'r') as f:
            content = f.read()
        return f"Dosya İçeriği:<br><pre>{content}</pre>"
    except FileNotFoundError:
        return 'Dosya bulunamadı.'


if __name__ == '__main__':
    global F1
    app.run(debug=True)
