const kue = require('kue');
const queue = kue.createQueue({name: 'push_notification_code'});

const obj = {
  phoneNumber: '0701036544',
  message: 'we go bro'
}

const job = queue.create('push_notification_code', obj)
	.save((err) => {
	 if (!err) {
	  console.log(`Notification job created: ${job.id}`);
	 }
	else {
	console.log('Notification job failed');
	}
	})

job.on('complete', (data) => {
	console.log('Notification job completed');
});
