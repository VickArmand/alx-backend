/**
 * a function named publishMessage:
 *      It will take two arguments: message (string), and time (integer - in ms)
 *      After time millisecond:
 *      The function should log to the console About to send MESSAGE
 *      The function should publish to the channel holberton school channel,
 *      the message passed in argument after the time passed in arguments
 */
import {print, createClient} from "redis";
const client = createClient();
const channel = 'holberton school channel';
client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});
client.on('ready', () => {
  console.log('Redis client connected to the server');
});

async function publishMessage(message, time) {
  setTimeout(() => {
    console.log(`About to send ${message}`);
    client.publish(channel, message);
  }, time);
}
publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);