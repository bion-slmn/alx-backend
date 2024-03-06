import createPushNotificationsJobs from './8-job.js';
import { createQueue } from 'kue';
const sinon = require('sinon');
const { expect } = require('chai');

const queue = createQueue();
const list = [{phoneNumber: '4153518780', message: 'This is the code 1234 to verify your account'},
	{phoneNumber: '4153518780', message: 'This is the code 1234 to verify your account'},
	{phoneNumber: '4153518780', message: 'This is the code 1234 to verify your account'}
];

describe('createPushNotification Job', function(){

  before(function() {
  queue.testMode.enter(true);
});

  afterEach(function() {
  queue.testMode.clear();
});

after(function() {
  queue.testMode.exit()
});

it('testing jobs in a queue', function(){
  try{
   createPushNotificationsJobs('list', queue);
  }
	catch (err) {
  expect(err.message).to.equal('Jobs is not an array');
  }
  
  createPushNotificationsJobs(list, queue);
  expect(queue.testMode.jobs.length).to.equal(3);
  expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
  expect(queue.testMode.jobs[0]).to.equal(list[0]);
});
});
