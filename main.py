from flask import Flask, request, jsonify
import os, time

app = Flask(__name__)
API_KEY = "mysecret123"

@app.route("/honeypot", methods=["POST", "GET"])
def honeypot():
    # accept both header styles
    key = request.headers.get("x-api-key") or request.headers.get("X-API-KEY")

    if key != API_KEY:
        return jsonify({
            "ok": False,
            "error": "Unauthorized"
        }), 401

    # accept any body (json or not)
    try:
        data = request.get_json(force=True, silent=True)
    except:
        data = None

    return jsonify({
        "ok": True,
        "status": "honeypot_active",
        "time": int(time.time()),
        "client_ip": request.remote_addr,
        "data": data
    }), 200


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
