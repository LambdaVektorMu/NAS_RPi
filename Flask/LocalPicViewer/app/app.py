from flask import Flask, render_template

app = Flask( __name__ )


@app.route('/')
@app.route('/top')
def top():
    return render_template('top.html')
