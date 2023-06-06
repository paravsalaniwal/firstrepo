const express = require('express');
const fetch = require('node-fetch');

const app = express();
const port = 3000;

app.use(express.static('public'));

app.get('/api/search', (req, res) => {
  const artistQuery = req.query.artist;

  fetch(`https://api.deezer.com/search/artist?q=${encodeURIComponent(artistQuery)}`)
    .then(response => response.json())
    .then(data => res.json(data))
    .catch(error => {
      console.error(error);
      res.status(500).json({ error: 'An error occurred' });
    });
});

app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
