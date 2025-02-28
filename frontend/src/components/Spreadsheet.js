 
import React, { useState } from 'react';
import './Spreadsheet.css';

const Spreadsheet = () => {
    const [data, setData] = useState({});
    
    return (
        <div className="spreadsheet">
            <table>
                <tbody>
                    {Object.keys(data).map((row, rowIndex) => (
                        <tr key={rowIndex}>
                            {Object.keys(data[row]).map((col, colIndex) => (
                                <td key={colIndex} contentEditable>{data[row][col]}</td>
                            ))}
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default Spreadsheet;