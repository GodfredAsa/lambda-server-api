import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Users')

def lambda_handler(event, context):
    user_id = event['pathParameters']['userId']
    response = table.get_item(Key={'userId': user_id})

    if 'Item' not in response:
        return {"statusCode": 404, "body": json.dumps({"message": "User not found"})}

    return {
        "statusCode": 200,
        "body": json.dumps(response['Item'])
    }
