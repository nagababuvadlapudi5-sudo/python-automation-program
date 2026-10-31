from flask import Flask

app = Flask(__name__)

def main():
    return "Hello world"

@app.route("/")
def home():
    return main()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
