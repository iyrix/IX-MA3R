from dynamorm import DynaModel
from marshmallow import fields, EXCLUDE
from django.conf import settings
import boto3
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Attr, Key
from rest_framework.response import Response

class List(DynaModel):
    class Table:
        resource_kwargs = {
            'endpoint_url': settings.DB_ENDPOINT
        }
        name = "List"
        hash_key = 'list_id'
        range_key = 'created_by'

    class Schema:
        list_id = fields.Str(primary_key=True)
        created_by = fields.Str()
        list_name = fields.Str()
    
    class Meta:
        unknown = EXCLUDE
    
    @classmethod
    def createList(cls, data):
        dynamodb = boto3.resource('dynamodb', endpoint_url=settings.DB_ENDPOINT)
        table = dynamodb.Table(cls.Table.name)
        try:
            response = table.scan(
                FilterExpression=Attr('list_id').eq(data['list_id'])
            )
            if(response['Count'] == 0):
                response = table.put_item(
                    Item=data
                )
                return Response({"Message": "Successfull created List"}, status=201)
            return Response({"Message": "List already exist."}, status=400)
        except ClientError as e:
            print('Error creating list: ', e)
    
    @classmethod
    def getAllList(cls):
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
            # return e.response['Error']['Message'];
        # try: 
            
        #     if response:
        #         print("User deleted successfully:", response)
        #         return response;
        #     return Response({"Message": "User with id does not exist."}, status=400)
        # except ClientError as e:
        #     print("Error deleting User:", e)
    
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
            
