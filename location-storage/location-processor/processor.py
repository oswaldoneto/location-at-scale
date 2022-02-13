import json

def process_receive_queue(event, context):

    message = event["Records"][0]["body"]
    print(type(message))

    data = json.loads(message)
    print(type(data))


    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
            # "location": ip.text.replace("\n", "")
        }),
    }
