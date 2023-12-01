from flask import Flask, render_template, request
import qrcode
from io import BytesIO
from base64 import b64encode

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def genORCode():
    url = request.form.get('url')
    qrCode = qrcode.make(url)

    memory = BytesIO()
    qrCode.save(memory)
    memory.seek(0)

    base64Img = "data:image/png;base64," + b64encode(memory.getvalue()).decode('ascii')

    return render_template('index.html', data=base64Img)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)