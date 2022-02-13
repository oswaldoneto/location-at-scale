
import json

def last_known_position(event, context):

    records = event['Records']
    for record in records:
        sns = record['Sns']
        message_id = sns['MessageId']
        message = json.loads(json.loads(sns["Message"]))


        device_id = message["DeviceId"]
        nmea_sentenses = message['NMEASentences']

        if len(nmea_sentenses) > 0:
            last_sentence = nmea_sentenses[-1]
            print(last_sentence)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Last known position successfully.",
        }),
    }
