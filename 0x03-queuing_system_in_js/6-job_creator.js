const kue = require("kue");
const q = kue.createQueue();

const jobData = {
  phoneNumber: "dads phone number",
  message: "where's the milk?",
};
const job = q
  .create("push_notification_code", jobData)
  .save((err) => {
    if (!err) console.log("Notification job created:", job.id);
  })
  .on("complete", () => console.log("Notification job completed"))
  .on("failed", () => console.log("Notification job failed"));
