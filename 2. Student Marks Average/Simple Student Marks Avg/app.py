from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET'])
def welcome():
    return "<h1> <strong>Hello</strong> World!</h1>"

@app.route('/pass/')
def passed():
    return "<h1> PASSED!! :) </h1>"

@app.route('/pass/<int:marks>', methods=['GET'])
def passedWithMark(marks):
    return " PASSED!! :) with marks " + str(marks)

@app.route('/fail/')
def failed():
    return "<h1> Failed!! :( </h1>"

@app.route('/fail/<int:marks>', methods=['GET'])
def failedWithMark(marks):
    return " FAILED!! :) with marks " + str(marks)

@app.route('/forms', methods=['GET', 'POST'])
def handleForm():
    if request.method == 'GET':
        return render_template('forms.html', avgMarks=0)
    else:
        maths=float(request.form['maths'])
        science=float(request.form['science'])
        history=float(request.form['history'])

        average_marks = (maths+science+history)/3

        # return render_template('forms.html', avgMarks=average_marks)
        res = "";
        if(average_marks>=33):
            res = "passed"
        else:
            res = "failed"

        return redirect(url_for(res, marks=average_marks))
    
@app.route('/api', methods=['POST'])
def api():
    data = request.get_json()
    data = dict(data)
    print(data)
    a_val = float(data['a'])
    b_val = float(data['b'])
    return jsonify(a_val+b_val)
        

if __name__ == '__main__':
    app.run(debug=True)