const express = require('express');
const axios = require('axios');
const router = express.Router();

// Environment variables
require('dotenv').config();

// Route to handle text generation requests
router.post('/generate-text', async (req, res) => {
  try {
    const { prompt } = req.body;
    if (!prompt) {
      return res.status(400).json({ message: 'No prompt provided' });
    }

    const response = await axios.post('https://api.openai.com/v1/chat/completions', {
      model: "gpt-3.5-turbo",
      messages: [{ role: "user", content: prompt }],
      temperature: 0.7
    }, {
      headers: {
        'Authorization': `Bearer ${process.env.OPENAI_API_KEY}`
      }
    });

    res.json(response.data);
  } catch (error) {
    console.error('Error in /generate-text:', error.response ? error.response.data : error.message);
    res.status(500).json({ message: 'Error processing your request' });
  }
});



// Test route
router.get('/test', (req, res) => {
  res.send('Test route is working!');
});

module.exports = router;
