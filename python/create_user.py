import json
import uuid
import boto3
from datetime import datetime
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Users')

def lambda_handler(event, context):
    data = json.loads(event['body'])
    name = data.get('name')
    email = data.get('email')

    if not name or not email:
        return {
            "statusCode": 400,
            "body": json.dumps({"message": "Name and email are required"})
        }

    # Check email uniqueness using GSI
    response = table.query(
        IndexName='EmailIndex',
        KeyConditionExpression=Key('email').eq(email)
    )

    if response['Items']:
        return {
            "statusCode": 400,
            "body": json.dumps({"message": "Email already in use"})
        }

    user = {
        'userId': str(uuid.uuid4()),
        'name': name,
        'email': email,
        'createdAt': datetime.utcnow().isoformat()
    }

    table.put_item(Item=user)

    return {
        "statusCode": 201,
        "body": json.dumps(user)
    }
