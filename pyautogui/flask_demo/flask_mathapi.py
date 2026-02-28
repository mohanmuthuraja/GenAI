from flask import Flask, request, jsonify

app = Flask(__name__)

# ------------------------
# Addition
# ------------------------
@app.route("/add", methods=["GET"])
def add():
    a = float(request.args.get("a"))
    b = float(request.args.get("b"))
    result = a + b
    return jsonify({"operation": "addition", "result": result})


# ------------------------
# Subtraction
# ------------------------
@app.route("/sub", methods=["GET"])
def sub():
    a = float(request.args.get("a"))
    b = float(request.args.get("b"))
    result = a - b
    return jsonify({"operation": "subtraction", "result": result})


# ------------------------
# Multiplication
# ------------------------
@app.route("/mul", methods=["GET"])
def mul():
    a = float(request.args.get("a"))
    b = float(request.args.get("b"))
    result = a * b
    return jsonify({"operation": "multiplication", "result": result})


# ------------------------
# Division
# ------------------------
@app.route("/div", methods=["GET"])
def div():
    a = float(request.args.get("a"))
    b = float(request.args.get("b"))

    if b == 0:
        return jsonify({"error": "Division by zero not allowed"}), 400

    result = a / b
    return jsonify({"operation": "division", "result": result})


# Run server
if __name__ == "__main__":
    app.run(debug=True)