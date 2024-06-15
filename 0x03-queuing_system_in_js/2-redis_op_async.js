/**
 * Using promisify,
 * modify the function displaySchoolValue to use ES6 async / await
 */
import {print, createClient} from "redis";
import util from 'util';
const client = createClient();
client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});
client.on('ready', () => {
  console.log('Redis client connected to the server');
});
function setNewSchool(schoolName, value) {
  client.set(schoolName, value, print);
}
async function displaySchoolValue(schoolName) {
  const asyncGet = util.promisify(client.get).bind(client);
  const value = await asyncGet(schoolName);
  console.log(value);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');