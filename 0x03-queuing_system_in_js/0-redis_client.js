#!/usr/bin/env node

import { createClient } from 'redis';

const client = createClient();

client.connect()
    .then(() => {
        console.log("Redis client connected to the server");
    }).catch((err) => {
        console.log(`Redis client not connected to the server: ${err}`);
    })
