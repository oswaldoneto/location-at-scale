
import json

def receive(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "helo world",
        }),
    }
