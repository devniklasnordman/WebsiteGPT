import React, { useState } from 'react';
import axios from 'axios';
import '../styling/components/GameWizard.css'; // Import the CSS file
import gameImage from '../images/Game_Wizard.png'; // Import your image


function GameWizard() {
  const [query, setQuery] = useState('');
  const [response, setResponse] = useState('');

  const handleSubmit = async (event) => {
    event.preventDefault();
    setResponse('Fetching response...');  // Indicate loading status
    try {
      const res = await axios.post('http://localhost:3001/api/ask-assistant', { prompt: query });
      console.log('API response:', res); // Log the entire response
      setResponse(res.data.reply.response);
      console.log('Response state:', response); // Log the state
    } catch (error) {
      console.error('Error fetching response:', error);
      setResponse('Failed to get response from the assistant. Please try again.');
    }
  };

  return (
    <div className="game-wizard-container">
      <div className="centered-content">
        <h1>Welcome to Video Game Wizard - International Sales Statistics</h1>
        <p>Explore video game sales statistics and trends with the power of AI.</p>
      </div>

      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Ask a question about video game sales..."
        />
        <button type="submit">Ask the Wizard</button>
      </form>

      {/* Render the response */}
      {response && (
        <div>
          <h3>Response:</h3>
          <p style={{ whiteSpace: 'pre-wrap' }}>{response}</p>

          {/* Display the image beneath the form */}
          <img src={gameImage} alt="Game" className="game-image" />
        </div>
      )}
    </div>
  );
}

export default GameWizard;
