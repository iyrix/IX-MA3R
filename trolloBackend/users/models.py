from dynamorm import DynaModel
from marshmallow import fields, EXCLUDE
from django.conf import settings
import boto3
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Attr
from rest_framework.response import Response

class User(DynaModel):
    class Table:
        resource_kwargs = {
            'endpoint_url': settings.DB_ENDPOINT
        }
        name = settings.DB_TABLE
        hash_key = 'id'

    class Schema:
        id = fields.Str(primary_key=True)
        username = fields.Str()
        email = fields.Email()
        password = fields.Str()
    
    class Meta:
        unknown = EXCLUDE
    
    @classmethod
    def createUser(cls, data):
        dynamodb = boto3.resource('dynamodb', endpoint_url=settings.DB_ENDPOINT)
        table = dynamodb.Table(cls.Table.name)
        try:
            response = table.scan(
                FilterExpression= Attr('email').eq(data['email'])
            )
            if(response['Count'] == 0):
                print("response['Count']", response['Count'])
                response = table.put_item(
                    Item=data
                )
                print("User created successfully:", response)
                return Response({"Message": "Successfull"}, status=201)
            return Response({"Message": "User with email already exist."}, status=400)
        except ClientError as e:
            print("Error creating user:", e)
    
    @classmethod
    def getAllUsers(cls):
        dynamodb = boto3.resource('dynamodb', endpoint_url=settings.DB_ENDPOINT)
        table = dynamodb.Table(cls.Table.name)
        try: 
            response = table.scan()
            items = response.get('Items', [])
            return items;
        except ClientError as e:
            print("Error fetching user:", e)
            return e;
    
    @classmethod
    def deleteUser(cls, id):
        dynamodb = boto3.resource('dynamodb', endpoint_url=settings.DB_ENDPOINT)
        table = dynamodb.Table(cls.Table.name)
        try: 
            response = table.delete_item(
                Key={
                    'id': id,
                }
            )
            print(response, "response===>")
        except ClientError as e:
            print(e.response['Error']['Message'])

    
    @classmethod
    def updateUser(cls, id, data):
        dynamodb = boto3.resource('dynamodb', endpoint_url=settings.DB_ENDPOINT)
        table = dynamodb.Table(cls.Table.name)
        try:
            table.update_item(
                Key={
                    'id': id,
                },
                UpdateExpression='SET username = :val1',
                ExpressionAttributeValues={
                    ':val1': data['username']
                }
            )
        except ClientError as e:
            print(e.response['Error']['Message'])
            
