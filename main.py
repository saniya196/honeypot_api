from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Change this if you want a new key
API_KEY = "mysecret123"

@app.route("/honeypot", methods=["GET", "POST"])
def honeypot():
    # Accept both header styles
    key = request.headers.get("x-api-key") or request.headers.get("X-API-KEY")

    if key != API_KEY:
        return jsonify({"error": "Unauthorized"}), 401

    # Read JSON body if present
    data = {}
    if request.is_json:
        try:
            data = request.get_json()
        except:
            data = {}

    return jsonify({
        "status": "ok",
        "message": "Honeypot triggered",
        "ip": request.remote_addr,
        "payload": data
    }), 200


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
