
import json
import boto3
import os

sqs = boto3.resource('sqs')

RECEIVE_QUEUE = os.environ['RECEIVE_QUEUE']

def receive(event, context):

    # it validates request body that must be present
    if not "body" in event or not event["body"]:
        return {
            "statusCode": 422
        }

    # it gets data from the body
    data = event["body"]
    
    # it gets queue from environment variable 
    queue = sqs.get_queue_by_name(QueueName=RECEIVE_QUEUE)

    print(queue)

    # it sends data to sqs queue 
    queue.send_message(MessageBody=data)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Location received successfully.",
        }),
    }