 function createPushNotificationsJobs(jobs, queue){
 if (!Array.isArray(jobs)) {
  throw new Error('Jobs is not an array');
 }

  jobs.forEach(value => {
    const job = queue.create('push_notification_code_3', value)

    job.on('enqueue', () => {
	       console.log(`Notification job created: ${job.id}`)
    	})
	.on('completed', (results) => {
	        console.log(`Notification job ${job.id} completed`);
	})
	.on('failed', err => {
		console.log(`Notification job ${job.id} failed: ${err}`)})
	.on('progress', (progress, data) => {
	  console.log(`Notification job ${job.id} ${progress}% complete`);
	}).save();
  });
}

module.exports = createPushNotificationsJobs;
