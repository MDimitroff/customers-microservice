from flask import Flask, request, jsonify
import boto3
from datetime import datetime

app = Flask(__name__)

@app.route('/api/customers', methods=['POST'])
def create_customer():
    '''
    Request body looks like this
    {
        'name': 'John Doe',dock
        'username': 'johndoe'
    }
    '''
    # Validation
    if not 'name' in request.json or not 'username' in request.json:
        return 'Incorrect input data. Provide both name and username'
        
    # set up DynamoDB connection and get the table
    dynamodb = boto3.resource('dynamodb', region_name='eu-central-1') # aws_access_key_id='xxx', aws_secret_access_key='xxx'
    table = dynamodb.Table('customers')

    # Set customer's registration date
    request.json['date'] = datetime.now().strftime("%d.%m.%Y %H:%M:%S")

   # Create record in table
    table.put_item(Item=request.json)     

    return 'Customer saved'


if __name__ == "__main__":
    app.run()