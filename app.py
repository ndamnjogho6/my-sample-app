import os
import json
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def get_secret():
    # The secret is injected into the environment as a JSON string
    secret_str = os.getenv("MY_SECRET_VALUE")
    try:
        # Parse the string to a dictionary
        secret_dict = json.loads(secret_str)
        # Return only the value
        return jsonify({
            "message": "Secret pulled successfully",
            "secret": secret_dict.get("MY_SECRET_VALUE")
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
