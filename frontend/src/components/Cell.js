 
import React from 'react';

const Cell = ({ value, onChange }) => {
    return (
        <td contentEditable onBlur={(e) => onChange(e.target.innerText)}>{value}</td>
    );
};

export default Cell;