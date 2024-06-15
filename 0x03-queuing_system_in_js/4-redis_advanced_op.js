/**
 * Create Hash:
 * Using hset, let’s store the following:
 * The key of the hash should be HolbertonSchools
 * It should have a value for:
 * Portland=50, Seattle=80, New York=20, Bogota=20, Cali=40, Paris=2
 * Make sure you use redis.print for each hset
 * Display Hash: Using hgetall, display the object stored in Redis*/

import {print, createClient} from "redis";
import util from 'util';
const client = createClient();
client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});
client.on('ready', () => {
  console.log('Redis client connected to the server');
});
client.hset('HolbertonSchools', 'Portland', 50, print);
client.hset('HolbertonSchools','Seattle', 80,print);
client.hset('HolbertonSchools','New York', 20,print);
client.hset('HolbertonSchools','Bogota', 20,print);
client.hset('HolbertonSchools','Cali', 40,print);
client.hset('HolbertonSchools','Paris', 2, print);
client.hgetall('HolbertonSchools', (err, result) => console.log(result));
