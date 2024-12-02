#!/usr/bin/yarn dev

import { createdClient } from 'redis';

const client = createdClient();

client.on('connect', () => {
    console.log('Redis client connected to the server');
});

client.on('error', (err) => {
    console.log(`Redis client not connected to the server:`, err.toString());
});
