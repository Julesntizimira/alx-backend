const kue = require("kue");
const q = kue.createQueue();

function sendNotification(phoneNumber, message) {console.log(`Sending notification to ${phoneNumber}, with message: ${message}`)}
q.process('push_notification_code', (job) => {
    sendNotification(job.data.phoneNumber, job.data.message)
})