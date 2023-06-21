import boto3
import os


def send_message_to_query(message_body):
    aak = os.getenv("AWS_ACCESS_KEY")
    ask = os.getenv("AWS_SECRET_ACCESS_KEY")
    queue_url = os.getenv("AWS_SQS_URL")

    session = boto3.Session(
        aws_access_key_id=aak,
        aws_secret_access_key=ask,
        region_name='eu-central-1'
    )

    sqs = session.client('sqs')

    response = sqs.send_message(
        QueueUrl=queue_url,
        MessageBody=message_body
    )

    return response['MessageId']
