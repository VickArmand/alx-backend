/**
 * Create a queue with Kue
 * Create an object containing the Job data with the following format:
 * {phoneNumber: string,message: string,}
 * Create a queue named push_notification_code, and create a job with the object created before
 * When the job is created without error, log to the console Notification job created: JOB ID
 * When the job is completed, log to the console Notification job completed
 * When the job is failing, log to the console Notification job failed
 */
import kue from 'kue';
const queue = kue.createQueue({name: 'push_notification_code'});
const obj = {
    phoneNumber: '+254701234567',
    message: 'Testing job',
};
const job = queue.createJob('push_notification_code', obj);
job.on('enqueue', () => {
  console.log('Notification job created:', job.id);
});
job.on('complete', () => {
    console.log('Notification job completed');
});
job.on('failed attempt', () => {
    console.log('Notification job failed');
});
job.save();
