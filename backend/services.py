 
def evaluate_formula(expression):
    """Evaluate mathematical expressions safely"""
    try:
        return eval(expression, {"__builtins__": {}}, {})
    except Exception as e:
        raise ValueError(f"Invalid expression: {str(e)}")

# React Frontend (Cell.js)
import React from 'react';

const Cell = ({ value, onChange }) => {
    return (
        <td contentEditable onBlur={(e) => onChange(e.target.innerText)}>{value}</td>
    );
};

export default Cell;