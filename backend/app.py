from flask import Flask, render_template

app = Flask(__name__, template_folder="../frontend")

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


__name__ = "__main__"
app.run(debug=True)