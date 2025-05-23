const db = require('./utils/dbClient');

exports.handler = async (event) => {
  const { userId } = event.pathParameters;

  const result = await db.get({
    TableName: 'Users',
    Key: { userId }
  }).promise();

  return {
    statusCode: result.Item ? 200 : 404,
    body: JSON.stringify(result.Item || { message: 'User not found' }),
  };
};
