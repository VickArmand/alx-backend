/**
 * should subscribe to the channel holberton school channel
 * When it receives message on the channel holberton school channel,
 * it should log the message to the console
 * When the message is KILL_SERVER, it should unsubscribe and quit
 */
import {print, createClient} from "redis";
const client = createClient();
client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});
client.on('ready', () => {
  console.log('Redis client connected to the server');
});
const channel = 'holberton school channel';
client.on('message', (channel, message) => {
  console.log(message)
  if (message === 'KILL_SERVER') {
    client.unsubscribe(channel);
    client.end(true);
  }
});
client.subscribe(channel);
