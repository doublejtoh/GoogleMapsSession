from flask import Flask,render_template


app = Flask(__name__)

@app.route('/')
def index():
    return 'hello,flask!'
@app.route('/gmap')
def gmap():
    return render_template('gmap.html')
@app.route('/local_info')
def local_info():
    return render_template('local_info.html')
@app.route('/local_info2')
def local_info2():
    return render_template('local_info2.html')
if __name__ == '__main__':
    app.run(debug=True)
