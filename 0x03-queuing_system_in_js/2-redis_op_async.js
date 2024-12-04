#!/usr/bin/yarn dev
import { promisify } from 'util';
import { createClient, print } from 'redis';
import { futimesSync } from 'fs';

const client = createClient();

client.on('error', (err) => {
    console.log('Redis client not connected to the server:', err.toString());
});

const setNewSchool = (schoolName) => {
    client.SET(schoolName, value, print);
};

const displaySchoolValue = (schoolName) => {
    console.log(await promisify(client.GET).bind(client)(schoolName));
};

async function main() {
    await displaySchoolValue('Holberton');
    setNewSchool('HolbertonSanFrancisco', '100');
    await displaySchoolValue('HolbertonSanFrancisco');
}

client.on('connect', async () => {
    console.log('Redis client connnected to the server');
    await main();
})
