from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory database
employees = []

# 1️⃣ Add Employee
@app.route("/employee", methods=["POST"])
def add_employee():
    data = request.get_json()

    emp = {
        "id": data.get("id"),
        "name": data.get("name"),
        "department": data.get("department"),
        "salary": data.get("salary")
    }

    # Validation
    if not emp["id"] or not emp["name"]:
        return jsonify({"error": "ID and Name are required"}), 400

    employees.append(emp)
    return jsonify({"message": "Employee added successfully"}), 201


# 2️⃣ Get All Employees
@app.route("/employees", methods=["GET"])
def get_employees():
    return jsonify(employees)


# 3️⃣ Search Employee by ID
@app.route("/employee/<emp_id>", methods=["GET"])
def get_employee(emp_id):
    for emp in employees:
        if emp["id"] == emp_id:
            return jsonify(emp)
    return jsonify({"error": "Employee not found"}), 404


# 4️⃣ Delete Employee
@app.route("/employee/<emp_id>", methods=["DELETE"])
def delete_employee(emp_id):
    global employees
    employees = [emp for emp in employees if emp["id"] != emp_id]
    return jsonify({"message": "Employee deleted (if existed)"})


if __name__ == "__main__":
    app.run(debug=True)