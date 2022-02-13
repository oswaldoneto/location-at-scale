import json
import os
from datetime import datetime
import time
import uuid

import boto3

LOCATION_TABLE = os.environ['LOCATION_TABLE']
LAST_LOCATION_TOPIC = os.environ['LAST_LOCATION_TOPIC']

dynamodb = boto3.resource('dynamodb')
sns = boto3.client('sns')

def process_receive_queue(event, context):

    table = dynamodb.Table(LOCATION_TABLE)

    message = event["Records"][0]["body"]
    for record in event["Records"]:
        message = record["body"]

        data = json.loads(message)

        id = str(uuid.uuid4())
        timestamp = datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S.%f')
        data.update({
            'Id':id,
            'Timestamp': timestamp,
        })

        table.put_item(Item=data)

        print("Data persistido com sucesso")

        sns.publish(
            TopicArn=LAST_LOCATION_TOPIC,
            Message=json.dumps({"default": json.dumps(message)}),
            MessageStructure='json'        
        )

        print("Dado enviado por broadcast")

    
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Locations stored successfuly",
        }),
    }
