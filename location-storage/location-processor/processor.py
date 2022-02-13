import json
import os
from datetime import datetime
import time
import uuid

import boto3

LOCATION_TABLE = os.environ['LOCATION_TABLE']

dynamodb = boto3.resource('dynamodb')

def process_receive_queue(event, context):

    table = dynamodb.Table(LOCATION_TABLE)

    message = event["Records"][0]["body"]
    for record in event["Records"]:
        message = record["body"]

        data = json.loads(message)

        id = str(uuid.uuid4())
        timestamp = datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S.%f')
        data.update({
            'id':id,
            'timestamp': timestamp,
        })

        table.put_item(Item=data)
    
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Locations stored successfuly",
        }),
    }
