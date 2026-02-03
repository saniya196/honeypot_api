from flask import Flask, request, jsonify

app = Flask(__name__)
API_KEY = "mysecret123"

@app.route("/honeypot", methods=["GET"])
def honeypot():
    key = request.headers.get("X-API-KEY")
    if key != API_KEY:
        return jsonify({"error": "Unauthorized"}), 401

    return jsonify({
        "status": "triggered",
        "message": "Honeypot accessed",
        "ip": request.remote_addr
    })

import os
from flask import Flask, request, jsonify

app = Flask(__name__)
API_KEY = "mysecret123"

@app.route("/honeypot", methods=["GET"])
def honeypot():
    key = request.headers.get("X-API-KEY")
    if key != API_KEY:
        return jsonify({"error": "Unauthorized"}), 401

    return jsonify({
        "status": "triggered",
        "message": "Honeypot accessed",
        "ip": request.remote_addr
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

