const { createClient } = require('redis');

const client = createClient();

// Listen for errors
client.on('error', err => console.log(`Redis client error: ${err.message}`));
console.log('Redis client connected to the server');
