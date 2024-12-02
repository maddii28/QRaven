from flask import Flask, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Dynamic QR Code App"

# Run the app
if __name__ == "__main__":
    app.run(debug=True)