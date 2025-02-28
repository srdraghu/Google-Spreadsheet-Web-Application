 from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import numpy as np
import openpyxl

app = Flask(__name__)
CORS(app)

sheets = {}

@app.route("/sheets", methods=["POST"])
def create_sheet():
    """Create a new sheet"""
    sheet_id = str(len(sheets) + 1)
    sheets[sheet_id] = pd.DataFrame(np.nan, index=range(20), columns=[chr(i) for i in range(65, 75)])
    return jsonify({"sheet_id": sheet_id, "data": sheets[sheet_id].fillna(" ").to_dict()}), 201

@app.route("/sheets/<sheet_id>", methods=["GET"])
def get_sheet(sheet_id):
    """Retrieve a sheet"""
    if sheet_id in sheets:
        return jsonify({"data": sheets[sheet_id].fillna(" ").to_dict()})
    return jsonify({"error": "Sheet not found"}), 404

@app.route("/cells/<sheet_id>", methods=["PUT"])
def update_cell(sheet_id):
    """Update a cell's value"""
    if sheet_id not in sheets:
        return jsonify({"error": "Sheet not found"}), 404
    
    data = request.json
    row, col, value = data.get("row"), data.get("col"), data.get("value")
    if row is None or col is None or value is None:
        return jsonify({"error": "Invalid input"}), 400
    
    sheets[sheet_id].at[int(row), col] = value
    return jsonify({"message": "Cell updated"}), 200

@app.route("/evaluate", methods=["POST"])
def evaluate_expression():
    """Evaluate formulas like SUM(A1:A5)"""
    data = request.json
    expression = data.get("expression")
    try:
        result = eval(expression, {"__builtins__": {}}, {})
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
