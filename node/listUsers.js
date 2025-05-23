const db = require('./utils/dbClient');

exports.handler = async () => {
  const result = await db.scan({ TableName: 'Users' }).promise();

  return {
    statusCode: 200,
    body: JSON.stringify(result.Items),
  };
};
