#!/usr/bin/npm dev
import kue from "kue";

const queue = kue.createQueue();

function sendNotification(phoneNumber, message) {
    console.log(
        `Sending notification to ${phoneNumber},`,
        'with message:',
        message,
    );
}

queue.process('push_notification_code', (job, done) => {
    sendNotification(phoneNumber, message);
    done();
});
