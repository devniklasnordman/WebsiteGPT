// App.js
import React from 'react';
import { BrowserRouter as Router, Routes, Route, Outlet } from 'react-router-dom';
import GPT3Test from './components/GPT3Test'; // Import your GPT3Test component
import GameWizard from './components/GameWizard'; // Import your GameWizard component

function App() {
  return (
    <Router>
      <div>
        <Routes>
          <Route path="/" element={<Outlet />}>
            <Route index element={<GPT3Test />} /> {/* Use GPT3Test as the index component */}
            <Route path="gamewizard" element={<GameWizard />} /> {/* Use GameWizard for the /gamewizard route */}
          </Route>
        </Routes>
      </div>
    </Router>
  );
}

export default App;
