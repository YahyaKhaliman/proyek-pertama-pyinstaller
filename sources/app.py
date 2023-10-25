from flask import Flask

app = Flask(__name)

@app.route('/')
def hello():
    return "Submission CI/CD Dicoding 2023 Yahya Khaliman Indrayana"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
