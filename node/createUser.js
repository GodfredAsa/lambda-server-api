const { v4: uuidv4 } = require('uuid');
const db = require('./utils/dbClient');

exports.handler = async (event) => {
  const { name, email } = JSON.parse(event.body);
  
  const emailCheck = await db.query({
    TableName: 'Users',
    IndexName: 'EmailIndex',
    KeyConditionExpression: 'email = :email',
    ExpressionAttributeValues: {
      ':email': email
    }
  }).promise();

  if(emailCheck.Items.length > 0) {
    return {
      statusCode: 400,
      body: JSON.stringify({ message: 'Email already in use' })
    };
  }

  // 2. Create the new user
  const user = {
    userId: uuidv4(),
    name,
    email,
    createdAt: new Date().toISOString()
  };

  await db.put({ TableName: 'Users', Item: user }).promise();

  return {
    statusCode: 201,
    body: JSON.stringify(user),
  };
};
