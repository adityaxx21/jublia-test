import React, { useState, useEffect } from "react";
import "../App.css";
import MyButton from "../components/MyButton";
import { recipientAPI } from "../API/recipientAPI";

function RecipientPage() {
  const [formData, setFormData] = useState({
    email: "",
  });

  const [tableData, setTableData] = useState([]); // Initialize tableData state with an empty array

  useEffect(() => {
    const fetchData = async () => {
      try {
        const data = await recipientAPI("GET"); // Call the getEmails function from the service to fetch emails
        setTableData(data.data); // Set the fetched data to the tableData state
      } catch (error) {
        // Handle errors
        console.error("Error fetching emails:", error);
      }
    };

    fetchData(); // Fetch data when the component mounts
  }, []);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const data = await recipientAPI("POST", formData);
      setTableData([...tableData, data.data]);
      setFormData({
        email: "",
      });
    } catch (error) {
      setFormData({
        email: formData.email,
      });
      console.error("Error adding email:", error);
    }
  };

//   const handleUpdate = (e) => {
//     e.preventDefault();
//     // Implement logic to update data
//     setShowUpdateCard(false); // Close the update card after updating
//   };

//   const handleCancel = () => {
//     setShowUpdateCard(false); // Close the update card when canceling
//   };

  const handleDelete = async (id, index) => {
    // Implement logic to confirm deletion
    const isConfirmed = window.confirm(
      "Are you sure you want to delete this item?"
    );
    if (isConfirmed) {
      recipientAPI("DELETE", null, id);
      const newData = [...tableData];
      console.log(index);
      newData.splice(index, 1);
      setTableData(newData);
    }
  };

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-3xl font-bold mb-4">Recepient Tables</h1>
      <form onSubmit={handleSubmit} className="mb-4">
        <label className="block mb-2">
          Email:
          <input
            type="email"
            name="email"
            value={formData.email}
            onChange={handleChange}
            className="block w-full border-gray-300 rounded-md mt-1"
            required
          />
        </label>
        <MyButton />
      </form>
      <h2 className="text-2xl font-bold mb-2">Table</h2>
      <table className="w-full">
        <thead>
          <tr className="bg-gray-200">
            <th className="border px-4 py-2">Email</th>
            <th className="border px-4 py-2">Action</th>
          </tr>
        </thead>
        <tbody>
          {tableData.map((data, index) => (
            <tr key={index}>
              <td className="border px-4 py-2">
                <div className="flex items-center">
                  <span>{data.email}</span>
                </div>
              </td>
              <td className="border px-4 py-2" style={{ width: "20%" }}>
                <button
                  onClick={() => handleDelete(data.id, index)}
                  className="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded"
                >
                  Delete
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default RecipientPage;
