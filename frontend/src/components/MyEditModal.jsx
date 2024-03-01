// Modal.js
import React from 'react';
import { Modal } from 'flowbite-react';

const MyEditModal = ({ show, onHide, item, editedName, editedPrice, setEditedName, setEditedPrice, handleSave, closeModal }) => {
  return (
    <Modal show={show} onHide={onHide}>
      <Modal.Header closeButton>
        <Modal.Title>Edit Item</Modal.Title>
      </Modal.Header>
      <Modal.Body>
        <form>
          <div className="form-group">
            <label>Name:</label>
            <input
              type="text"
              value={editedName}
              onChange={e => setEditedName(e.target.value)}
            />
          </div>
          <div className="form-group">
            <label>Price:</label>
            <input
              type="number"
              value={editedPrice}
              onChange={e => setEditedPrice(parseFloat(e.target.value))}
            />
          </div>
        </form>
      </Modal.Body>
      <Modal.Footer>
        <button onClick={handleSave}>Save</button>
        <button onClick={closeModal}>Cancel</button>
      </Modal.Footer>
    </Modal>
  );
};

export default MyEditModal;
