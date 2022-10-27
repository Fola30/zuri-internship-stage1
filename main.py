from flask import Flask, jsonify, render_template

app = Flask(__name__)


@app.route('/')
def home():
    data = jsonify(slackUsername='Fola23', backend=True, age=19, bio="My name is Rasheed, i am a backend developer "
                                                                     "who's always excited to learn new things.").json
    return render_template('index.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)