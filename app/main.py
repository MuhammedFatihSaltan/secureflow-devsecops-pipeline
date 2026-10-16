from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "healthy"}), 200


if __name__ == "__main__":
    # debug=False yapıyoruz (ileride güvenlik testi için değiştireceğiz)
    app.run(host="0.0.0.0", port=5000, debug=False)
