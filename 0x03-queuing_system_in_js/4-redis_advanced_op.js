const { createClient, print } = require('redis');

const client = createClient();

// Listen for errors
client.on('error', err => console.log(`Redis client error: ${err.message}`));
console.log('Redis client connected to the server');

//set hash key-value in HolbertonSchools list
client.hset('HolbertonSchools', 'Portland', '50', print);
client.hset('HolbertonSchools', 'Seattle', '80', print);
client.hset('HolbertonSchools', 'New York', '20', print);
client.hset('HolbertonSchools', 'Bogota', '20', print);
client.hset('HolbertonSchools', 'Cali', '40', print);
client.hset('HolbertonSchools', 'Paris', '2', print);

// retrieve all elements stored in HolbertonSchools list
client.hgetall('HolbertonSchools', function (error, result) {
  if (error) {
    console.log(error);
    throw error;
  }
  console.log(result);
});