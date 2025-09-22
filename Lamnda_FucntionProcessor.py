import json

def lambda_handler(event, context):
    # Validate that 'Records' exists in the event
    if 'Records' not in event:
        print("No 'Records' key in event. Event was:", json.dumps(event))
        return {
            'statusCode': 400,
            'body': json.dumps('Invalid event format: missing Records')
        }

    for record in event['Records']:
        try:
            # Parse the message body
            body = json.loads(record['body'])

            # Add a tag to indicate the source
            body['source'] = 'sqs'

            # Log the tagged message
            print("Processed message:", json.dumps(body))

        except KeyError as e:
            print(f"Missing key in record: {e}")
        except json.JSONDecodeError as e:
            print(f"Failed to decode JSON: {e}")

    return {
        'statusCode': 200,
        'body': json.dumps('Messages processed')
    }
print("Lambda 2 triggered by SQS")
