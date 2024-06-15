/**
 * Add two functions:
 * setNewSchool:
 *      It accepts two arguments schoolName, and value.
 *      It should set in Redis the value for the key schoolName
 *      It should display a confirmation message using redis.print
 * displaySchoolValue:
 *      It accepts one argument schoolName.
 *      It should log to the console the value for the key passed as argument
 */
import {createClient} from "redis";
const client = createClient();
client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});
client.on('ready', () => {
  console.log('Redis client connected to the server');
});
function setNewSchool(schoolName, value) {
  client.set(schoolName, value);
}
function displaySchoolValue(schoolName) {
  client.get(schoolName, (err, result) => console.log(result));
}
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');