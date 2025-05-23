import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Users')

def lambda_handler(event, context):
    user_id = event['pathParameters']['userId']
    table.delete_item(Key={'userId': user_id})
    
    return {"statusCode": 204}
