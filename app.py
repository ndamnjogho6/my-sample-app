import boto3
import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def get_secret():
    secret_name = os.environ.get("MY_SECRET_VALUE")
    region_name = os.environ.get("AWS_REGION", "us-east-1")

    client = boto3.client('secretsmanager', region_name=region_name)
    try:
        get_secret_value_response = client.get_secret_value(SecretId=secret_name)
        secret = get_secret_value_response['SecretString']
        return jsonify({"message": "Secret pulled successfully", "secret": secret})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

# Minor update to trigger GitHub Actions pipeline for deployment
