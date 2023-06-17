from flask import Flask, render_template, request
import algorithm

app = Flask(__name__)
inversions = None


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')

    if request.method == 'POST':
        arr = [request.form['pos1'], request.form['pos2'], request.form['pos3'], request.form['pos4'], request.form['pos5'],
               request.form['pos6'], request.form['pos7'], request.form['pos8'], request.form['pos9'], request.form['pos10']]
        inversions = algorithm.getInversions(arr)
        return render_template('index.html', inversions=inversions)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
