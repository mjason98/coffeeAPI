from dotenv import load_dotenv
import os
import boto3


load_dotenv()


MESSAGE_LEGACY = 'in future version, \
                 an email will be sent to this address :)'


def consume_email_messages():
    aak = os.getenv("AWS_ACCESS_KEY")
    ask = os.getenv("AWS_SECRET_ACCESS_KEY")
    queue_url = os.getenv("AWS_SQS_URL")

    session = boto3.Session(
        aws_access_key_id=aak,
        aws_secret_access_key=ask,
        region_name='eu-central-1'
    )

    sqs = session.client('sqs')

    while True:
        response = sqs.receive_message(
            QueueUrl=queue_url,
            MaxNumberOfMessages=1,
            WaitTimeSeconds=20
        )

        if 'Messages' in response:
            for message in response['Messages']:
                print("Received message:", message['Body'], MESSAGE_LEGACY)

                sqs.delete_message(
                    QueueUrl=queue_url,
                    ReceiptHandle=message['ReceiptHandle']
                )


if __name__ == '__main__':
    consume_email_messages()
