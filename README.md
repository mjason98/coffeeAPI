# Coffee API

A simple Flask coffee api.
[Here](guide/guide.md) is a guide on how to create an EC2 of the app and then an image of it.

### AWS SQS

For the AWS SQS to work, remember to fill the values for the env variables in a file named .env, use .env.example as a quide.

For the listener process, just run the following command:
```shell
python email_consumer.py
```
