from flask import Flask, render_template, request, send_file, jsonify, url_for
import itertools
import string
import pikepdf
import os
import time

app = Flask(__name__)

def brute_force_pdf(input_pdf, output_pdf, max_length, char_type):
    characters = {
        "Numbers": string.digits,
        "Alphabets": string.ascii_letters,
        "Alphanumeric": string.ascii_letters + string.digits,
    }
    
    selected_chars = characters[char_type]
    
    for length in range(1, max_length + 1):
        for password in itertools.product(selected_chars, repeat=length):
            password = ''.join(password)
            try:
                with pikepdf.open(input_pdf, password=password) as pdf:
                    pdf.save(output_pdf)
                    return password
            except pikepdf.PasswordError:
                pass
    return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    file = request.files['file']
    max_length = int(request.form['max_length'])
    char_type = request.form['char_type']
    
    input_pdf_path = os.path.join('uploads', file.filename)
    output_pdf_path = os.path.join('uploads', 'unlocked_' + file.filename)
    
    file.save(input_pdf_path)
    
    start_time = time.time()
    password = brute_force_pdf(input_pdf_path, output_pdf_path, max_length, char_type)
    end_time = time.time()
    
    if password:
        processing_time = end_time - start_time
        return jsonify({
            'success': True,
            'download_url': url_for('download_file', filename='unlocked_' + file.filename),
            'processing_time': round(processing_time, 2),
            'password': password
        })
    else:
        return jsonify({'success': False})

@app.route('/download/<filename>')
def download_file(filename):
    return send_file(os.path.join('uploads', filename), as_attachment=True)

if __name__ == '__main__':
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    app.run(debug=True)
