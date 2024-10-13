#!/usr/bin/env node

import { createClient } from 'redis';
import 'redis'

const client = createClient();

client.connect()
    .then(() => {
        console.log("Redis client connected to the server");
    }).catch((err) => {
        console.log(`Redis client not connected to the server: ${err}`);
    })


function setNewSchool(schoolName, value) {
    client.set(schoolName, value, redis.print);
}

function displaySchoolValue(schoolName) {
    client.get(schoolName, (err, value) => {
        if (!err) {
            console.log(value);
        }
    });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
