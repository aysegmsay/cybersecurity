from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

def upload_file(file_path):
    with open(file_path, 'wb') as f:
        # İstediğiniz dosya içeriğini burada belirleyin.
        f.write("Bu dosya sunucu tarafında yüklendi.")

@app.route('/')
def home():
    return render_template('cyber.html')

@app.route('/upload', methods=['POST'])
def upload_file_self():
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], 'self_uploaded.txt')
    upload_file(file_path)
    return redirect(url_for('view_file', filename='self_uploaded.txt'))

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
    app.run(debug=True)
