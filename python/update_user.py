import json
import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Users')

def lambda_handler(event, context):
    user_id = event['pathParameters']['userId']
    data = json.loads(event['body'])
    name = data.get('name')
    email = data.get('email')

    update_expr = []
    expr_attrs = {}

    if name:
        update_expr.append("name = :name")
        expr_attrs[':name'] = name

    if email:
        update_expr.append("email = :email")
        expr_attrs[':email'] = email

    if not update_expr:
        return {"statusCode": 400, "body": json.dumps({"message": "Nothing to update"})}

    response = table.update_item(
        Key={'userId': user_id},
        UpdateExpression="SET " + ", ".join(update_expr),
        ExpressionAttributeValues=expr_attrs,
        ReturnValues="ALL_NEW"
    )

    return {
        "statusCode": 200,
        "body": json.dumps(response['Attributes'])
    }
