// server.js

const express = require('express');
const { google } = require('googleapis');

const app = express();
app.use(express.urlencoded({ extended: true }));

// Load credentials from the downloaded JSON file
const credentials = require('projectfyp-388706-b9e079cdbdae.json');

// Create an OAuth2 client
const client = new google.auth.OAuth2(
  credentials.client_id,
  credentials.client_secret,
  credentials.redirect_uris[0]
);

// Authenticate with the client
client.setCredentials(credentials);

// Handle the form submission
app.post('/predict', (req, res) => {
  const formData = req.body; // Assuming form data is sent in the request body

  // Create a new row object with the form data
  const newRow = {
    values: [
      formData.field1,
      formData.field2,
      // Add more fields as needed
    ],
  };

  // Append the new row to the Google Sheet
  const sheets = google.sheets({ version: 'v4', auth: client });
  sheets.spreadsheets.values.append({
    spreadsheetId: '1XfpbylxHKKVsxs1q92NneDdhD62UuJ6D2LrGR6XoeKg',
    range: 'Sheet1!B2:M2', // Adjust the range as needed
    valueInputOption: 'RAW',
    resource: newRow,
  }, (err, response) => {
    if (err) {
      console.error(err);
      return res.status(500).send('Error occurred while updating the Google Sheet.');
    }

    console.log('Data posted to Google Sheet successfully.');
    res.status(200).send('Data posted to Google Sheet.');
  });
});

app.listen(3000, () => {
  console.log('Server is running on port 3000');
});
