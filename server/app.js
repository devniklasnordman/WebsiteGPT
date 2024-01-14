const express = require('express');
const cors = require('cors');
const gptRoutes = require('./routes/gptRoutes');
const GameWizardRoutes = require('./routes/GameWizardRoutes');
require('dotenv').config();

const app = express();


// Middleware
app.use(cors());
app.use(express.json());
app.use('/api', gptRoutes);
app.use('/api', GameWizardRoutes); // Include this line

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
