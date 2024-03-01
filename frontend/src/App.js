import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import EmailPage from './pages/EmailsPage';
import RecipientPage from './pages/RecipientPage';
import MySideBar from './components/MySideBar';

function App() {
  const sidebarLinks = [
    { to: '/', text: 'Home' },
    { to: '/recipient', text: 'Recipients' },
    // Add more links as needed
  ];
  return (
    <Router>
      <div className="flex h-screen overflow-hidden bg-gray-100">
        {/* Sidebar */}
        <MySideBar links={sidebarLinks}/>

        {/* Main content */}
        <div className="flex flex-col flex-1 w-full">
          <div className="h-full overflow-y-auto">
            <Routes>
              <Route path="/" element={<EmailPage />} />
              <Route path="/recipient" element={<RecipientPage />} />
              {/* Add more routes as needed */}
            </Routes>
          </div>
        </div>
      </div>
    </Router>
  );
}

export default App;
