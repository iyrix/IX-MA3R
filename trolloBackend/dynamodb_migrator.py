import os
import boto3
from django.conf import settings
from botocore.exceptions import ClientError

# Configure Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'trolloBackend.settings')

def User(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url=settings.DB_ENDPOINT)

    table = dynamodb.create_table(
        TableName=settings.DB_TABLE,
        KeySchema=[
            {
                'AttributeName': 'id',
                'KeyType': 'HASH'
            },
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'id',
                'AttributeType': 'S',
                
            },
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5,
        }
    )
    return table

def List(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url=settings.DB_ENDPOINT)
    table = dynamodb.create_table(
        TableName="List",
        KeySchema=[
            {
                'AttributeName': 'list_id',
                'KeyType': 'HASH'
            },
            {
                'AttributeName': 'created_by', 
                'KeyType': 'RANGE'
            },
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'list_id',
                'AttributeType': 'S',
            },
             {
                'AttributeName': 'created_by',
                'AttributeType': 'S',
            },
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5,
        }
    )
    return table

def Task(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url=settings.DB_ENDPOINT)
    table = dynamodb.create_table(
        TableName="Task",
        KeySchema=[
            {
                'AttributeName': 'task_id',
                'KeyType': 'HASH'
            },
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'task_id',
                'AttributeType': 'S',
            },
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5,
        }
    )
    return table


if __name__ == '__main__':
   
   #create user table 
    my_table = User()
    my_table.meta.client.get_waiter('table_exists').wait(TableName=settings.DB_TABLE)
    print(my_table.item_count)
    #create list table
    my_table = List()
    my_table.meta.client.get_waiter('table_exists').wait(TableName=settings.DB_TABLE)
    print(my_table.item_count)
    #create task table
    my_table = Task()
    my_table.meta.client.get_waiter('table_exists').wait(TableName=settings.DB_TABLE)
    print(my_table.item_count)
