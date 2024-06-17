/**
 * create a function named createPushNotificationsJobs:
 * It takes into argument jobs (array of objects), and queue (Kue queue)
 * If jobs is not an array, it should throw an Error with message: Jobs is not an array
 * For each job in jobs, create a job in the queue push_notification_code_3
 * When a job is created, it should log to the console Notification job created: JOB_ID
 * When a job is complete, it should log to the console Notification job JOB_ID completed
 * When a job is failed, it should log to the console Notification job JOB_ID failed: ERROR
 * When a job is making progress, it should log to the console Notification job JOB_ID PERCENT% complete
 */
export default function createPushNotificationsJobs(jobs, queue) {
  if (!(jobs instanceof Array))
    throw(new Error('Jobs is not an array'));
  jobs.forEach(job_obj => {
    const new_job = queue.create('push_notification_code_3', job_obj);
    new_job.on('enqueue', () => {
      console.log(`Notification job created: ${new_job.id}`);
    })
    .on('complete', () => {
      console.log(`Notification job ${new_job.id} completed`);
    })
    .on('progress', (progress, _data) => {
      console.log('Notification job', new_job.id, `${progress}% complete`);
    })
    .on('failed attempt', (err) => {
      console.log(`Notification job ${new_job.id} failed: ${err}`);
    }).save();
  });
}