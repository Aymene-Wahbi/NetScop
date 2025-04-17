from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    ip = request.form['ip']
    mask = request.form['mask']
    cidr = f"{ip}/{mask}"

    try:
        output = subprocess.check_output(['ipcalc', cidr], text=True)
    except subprocess.CalledProcessError:
        output = "Error running ipcalc. Please check the IP or mask."

    return render_template('result.html', cidr=cidr, output=output)

if __name__ == '__main__':
    app.run(debug=True, port=5000)