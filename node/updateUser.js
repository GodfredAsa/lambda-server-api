const db = require('./utils/dbClient');

exports.handler = async (event) => {
  const { userId } = event.pathParameters;
  const { name, email } = JSON.parse(event.body);

  const result = await db.update({
    TableName: 'Users',
    Key: { userId },
    UpdateExpression: 'set #name = :name, email = :email',
    ExpressionAttributeNames: { '#name': 'name' },
    ExpressionAttributeValues: {
      ':name': name,
      ':email': email
    },
    ReturnValues: 'ALL_NEW'
  }).promise();

  return {
    statusCode: 200,
    body: JSON.stringify(result.Attributes),
  };
};
