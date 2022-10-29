from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def home():
    return jsonify(slackUsername='Fola23', backend=True, age=19, bio="My name is Rasheed, i am a backend developer "
                                                                     "who's always excited to learn new things...")


if __name__ == '__main__':
    app.run(debug=True)