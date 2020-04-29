from flask import Flask, request, jsonify
import boto3

app = Flask(__name__)

@app.route('/api/create-customer', methods=['POST'])
def create_customer():
    '''
    Format of json request is
    {
        'name': 'John Doe',
        'username': 'johndoe'
    }
    '''
    data = request.json
    name = data['name']
    username = data['username']

    # set up DynamoDB connection
    dynamodb = boto3.resource('dynamodb', region_name='eu-central-1', aws_access_key_id='AKIAUBFFK6SOG24HUIFW', aws_secret_access_key='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')
    table = dynamodb.Table('customers')

   # Create the DynamoDB table.
    table.put_item(Item={
            'username': username,
            'name': name
        }
    )     

    return 'Customer saved'


if __name__ == "__main__":
    app.run()