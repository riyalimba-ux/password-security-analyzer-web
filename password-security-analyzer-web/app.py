from flask import Flask, render_template, request, jsonify
from checker import check_strength_advanced
from entropy import calculate_entropy, estimate_crack_time

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    password = data.get("password", "")

    strength, score, suggestions = check_strength_advanced(password)
    entropy = calculate_entropy(password)
    crack_time = estimate_crack_time(password)

    return jsonify({
        "strength": strength,
        "score": score,
        "entropy": entropy,
        "crack_time": crack_time,
        "suggestions": suggestions
    })

if __name__ == "__main__":
    app.run(debug=True)