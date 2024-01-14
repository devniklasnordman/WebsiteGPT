// GPT3Test.js
import React, { useState } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom'; // Import Link
import '../styling/components/GPT3Test.css'; // Import the CSS file

function GPT3Test() {
  const [inputText, setInputText] = useState('');
  const [response, setResponse] = useState('');

  const handleInputChange = (event) => {
    setInputText(event.target.value);
  };

  const handleSubmit = async () => {
    try {
      const result = await axios.post('http://localhost:3001/api/generate-text', { prompt: inputText });
      setResponse(result.data);
    } catch (error) {
      console.error('Error fetching response:', error);
      setResponse('Error: Unable to fetch response');
    }
  };

  return (
    <div className="gpt3-test-container">
      <h1>GPT-3 API Test Interface</h1>
      <input type="text" value={inputText} onChange={handleInputChange} />
      <button onClick={handleSubmit}>Submit</button>
      <p>Response:</p>
      {response.choices && response.choices.map((choice, index) => (
        <p key={index}>{choice.message.content}</p>
      ))}
      {/* Add a button to navigate to GameWizard */}
      <Link to="/gamewizard" className="nav-link">
        Go to GameWizard
        <div className="arrow-icon">→</div> {/* Right arrow icon */}
      </Link>
    </div>
  );
}

export default GPT3Test;
