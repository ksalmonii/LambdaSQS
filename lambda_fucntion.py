import json
import boto3

# Initialize SQS client with region
sqs = boto3.client('sqs', region_name='us-east-1')

# Replace with your actual SQS queue URL
QUEUE_URL = 'https://sqs.us-east-1.amazonaws.com/637423305058/ImageProcessingQueue'

def lambda_handler(event, context):
    try:
        # Extract data from the event object
        # For API Gateway HTTP requests, the body is in event['body']
        if 'body' in event:
            # Parse the JSON body if it exists
            body = json.loads(event['body'])
        else:
            # Use the event directly if it's from another source
            body = event
        
        # Extract required fields with error handling
        required_fields = ['imageName', 'userId', 'action']
        payload = {}
        
        for field in required_fields:
            if field not in body:
                return {
                    'statusCode': 400,
                    'body': json.dumps({
                        'error': f'Missing required field: {field}'
                    })
                }
            payload[field] = body[field]

        # Send the message to SQS
        response = sqs.send_message(
            QueueUrl=QUEUE_URL,
            MessageBody=json.dumps(payload)
        )

        # Return the MessageId in the response
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Message sent to SQS',
                'messageId': response['MessageId'],
                'payload': payload  # Optional: return the sent payload for confirmation
            })
        }

    except json.JSONDecodeError:
        return {
            'statusCode': 400,
            'body': json.dumps({
                'error': 'Invalid JSON format in request body'
            })
        }
    except Exception as e:
        # Handle any other errors
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': str(e)
            })
        }