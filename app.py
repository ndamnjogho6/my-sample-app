import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def get_secret():
    secret = os.getenv("MY_SECRET_VALUE")
    if secret:
        return jsonify({"message": "Secret pulled successfully", "secret": secret})
    else:
        return jsonify({"error": "Secret not found"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
