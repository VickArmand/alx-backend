/**
 * connect to the Redis server running on your machine
 * It should log to the console the message Redis client
 * connected to the server when the connection to Redis works correctly
 * It should log to the console the message Redis
 * client not connected to the server: ERROR_MESSAGE when the connection to Redis does not work
 */
import { createClient } from "redis";
const client = createClient();
client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});
client.on('ready', () => {
  console.log('Redis client connected to the server');
});
