const express = require('express');
const axios = require('axios');
const router = express.Router();

router.post('/ask-assistant', async (req, res) => {
    console.log("Received request:", req.body)
    try {
        const response = await axios.post('http://localhost:5001/ask', {
            prompt: req.body.prompt
        });
        res.json({ reply: response.data });
    } catch (error) {
        console.error(error);
        res.status(500).send('Error communicating with the assistant service');
    }
});

module.exports = router;
