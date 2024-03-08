from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_nuclei_fuzzer', methods=['POST'])
def run_nuclei_fuzzer():
    target = request.form['target']
    file = request.files['fileInput'] if 'fileInput' in request.files else None

    command = ['./NucleiFuzzer.sh']
    if target:
        command.extend(['-d', target])
    elif file:
        file.save('input.txt')
        command.extend(['-f', 'input.txt'])

    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout

if __name__ == '__main__':
    app.run(debug=True)
