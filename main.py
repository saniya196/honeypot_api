from flask import Flask, request, jsonify
import os
import time

app = Flask(__name__)

API_KEY = "mysecret123"

@app.route("/honeypot", methods=["POST"])
def honeypot():
    key = request.headers.get("x-api-key") or request.headers.get("X-API-KEY")
    if key != API_KEY:
        return jsonify({
            "success": False,
            "error": "Unauthorized"
        }), 401

    # Tester always sends JSON
    try:
        body = request.get_json(force=True)
    except:
        return jsonify({
            "success": False,
            "error": "Invalid JSON"
        }), 400

    response = {
        "success": True,
        "service": "honeypot",
        "status": "active",
        "timestamp": int(time.time()),
        "client_ip": request.remote_addr,
        "received": body
    }

    return jsonify(response), 200


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
