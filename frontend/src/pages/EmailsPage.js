import React, { useState, useEffect } from "react";
import "../App.css";
import MyButton from "../components/MyButton";
import { getEmails, postEmails } from "../API/emailsAPI";

function EmailPage() {
  const [formData, setFormData] = useState({
    event_id: "",
    email_subject: "",
    email_content: "",
    timestamp: "",
  });

  const [tableData, setTableData] = useState([]); // Initialize tableData state with an empty array

  useEffect(() => {
    const fetchData = async () => {
      try {
        const data = await getEmails(); // Call the getEmails function from the service to fetch emails
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
    const newValue = name === "event_id" ? parseInt(value, 10) : value;
    setFormData({ ...formData, [name]: newValue });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const data = await postEmails(formData)
      setTableData([...tableData, data.data]);
      setFormData({
        event_id: "",
        email_subject: "",
        email_content: "",
        timestamp: "",
      });
    } catch (error) {
      console.error("Error adding email:", error);
    }
  };

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-3xl font-bold mb-4">Emails Tables</h1>
      <form onSubmit={handleSubmit} className="mb-4">
        <label className="block mb-2">
          Event ID:
          <input
            type="number"
            name="event_id"
            value={formData.event_id}
            onChange={handleChange}
            className="block w-full border-gray-300 rounded-md mt-1"
            pattern="[0-9]*"
            required
          />
        </label>
        <label className="block mb-2">
          Email Subject:
          <input
            type="text"
            name="email_subject"
            value={formData.email_subject}
            onChange={handleChange}
            className="block w-full border-gray-300 rounded-md mt-1"
            required
          />
        </label>
        <label className="block mb-2">
          Email Content:
          <textarea
            id="email_content"
            name="email_content"
            value={formData.email_content}
            onChange={handleChange}
            className="block w-full border-gray-300 rounded-md mt-1"
            required
          />
        </label>
        <label htmlFor="datetime">
          Date and Time:
          <input
            type="datetime-local"
            id="timestamp"
            name="timestamp"
            value={formData.timestamp}
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
            <th className="border px-4 py-2">Event ID</th>
            <th className="border px-4 py-2">Email Subject</th>
            <th className="border px-4 py-2">Email Content</th>
            <th className="border px-4 py-2">Timestamp</th>
          </tr>
        </thead>
        <tbody>
          {tableData.map((data, index) => (
            <tr key={index}>
              <td className="border px-4 py-2">{data.event_id}</td>
              <td className="border px-4 py-2">{data.email_subject}</td>
              <td className="border px-4 py-2">{data.email_content}</td>
              <td className="border px-4 py-2">{data.timestamp}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default EmailPage;
