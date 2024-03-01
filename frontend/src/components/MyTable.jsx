import React from 'react';

function MyTable({ tableData, columnKeys }) {
  return (
    <tbody>
      {tableData.map((data, index) => (
        <tr key={index}>
          {columnKeys.map((key) => (
            <td key={key} className="border px-4 py-2">{data[key]}</td>
          ))}
        </tr>
      ))}
    </tbody>
  );
}

export default MyTable;
