
import json

def receive(event, context):

    if not "body" in event or not event["body"]:
        return {
            "statusCode": 422
        }

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": event,
        }),
    }
