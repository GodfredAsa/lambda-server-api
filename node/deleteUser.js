const db = require('./utils/dbClient');

exports.handler = async (event) => {
  const { userId } = event.pathParameters;

  await db.delete({
    TableName: 'Users',
    Key: { userId }
  }).promise();

  return {
    statusCode: 204,
    body: ''
  };
};
