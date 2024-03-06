import { createClient } from 'redis';
const redis =  require('redis');
const {promisify} = require('util');

const client = createClient();

client.on('connect', () => {
    console.log('Redis client connected to the server');
});

//client.on('error', err => {
//    console.error(`Redis client not connected to the server: ${err}`);
//});

const publisher = client.duplicate();

const publishMessage = (message, time)=> {
  console.log(`About to send ${message}`);
  setTimeout(() => {
    publisher.publish('holberton school channel', message) 
  }, time);
}

client.on('error', err => {
    console.error(`Redis client not connected to the server: ${err}`);
});

//module.exports = client;

publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);
