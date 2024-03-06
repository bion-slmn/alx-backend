import { createClient } from 'redis';

const client = createClient();

client.on('connect', () => {
    console.log('Redis client connected to the server');
});

client.on('error', err => {
    console.error(`Redis client not connected to the server: ${err}`);
});

const subscriber = client.duplicate();

subscriber.subscribe('holberton school channel')

subscriber.on('message', (_, message) => {
  console.log(message);
  if (message === 'KILL_SERVER'){
  subscriber.unsubscribe('holberton school channel');
  subscriber.quit();
  }
});

