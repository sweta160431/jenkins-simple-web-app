from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Automate code testing and deployment using a
Continuous Integration/Continuous Deployment (CI/CD) pipeline!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

