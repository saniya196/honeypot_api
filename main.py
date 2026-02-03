from flask import Flask, request, jsonify
import os, time, uuid

app = Flask(__name__)
API_KEY = "mysecret123"

@app.route("/honeypot", methods=["POST"])
def honeypot():
    key = request.headers.get("x-api-key") or request.headers.get("X-API-KEY")
    if key != API_KEY:
        return jsonify({
            "status": "error",
            "message": "Unauthorized",
            "code": 401
        }), 401

    # accept any json
    try:
        body = request.get_json(force=True, silent=True)
    except:
        body = None

    return jsonify({
        "status": "success",
        "code": 200,
        "service": "honeypot",
        "request_id": str(uuid.uuid4()),
        "timestamp": int(time.time()),
        "received": body
    }), 200


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
