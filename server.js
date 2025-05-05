const express = require('express');

const hostname = '127.0.0.1';
const port = 3000;

// Create Express application instance
const app = express();

// Define root endpoint that returns 'Hello, World!'
app.get('/', (req, res) => {
  res.status(200).contentType('text/plain').send('Hello, World!\n');
});

// Define new endpoint '/evening' that returns 'Good evening'
app.get('/evening', (req, res) => {
  res.status(200).contentType('text/plain').send('Good evening');
});

// Start the Express server
app.listen(port, hostname, () => {
  console.log(`Express server running at http://${hostname}:${port}/`);
});
