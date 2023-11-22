import graphene
from graphene_django.types import DjangoObjectType
from .models import Task
import boto3
from django.conf import settings
import uuid;
import json

dynamodb = boto3.resource('dynamodb', endpoint_url= settings.DB_ENDPOINT)

def save_to_dynamodb(tableName, **data):
    # Exclude any non-serializable types, such as ModelState
    serializable_data = {key: value for key, value in data.items() if is_serializable(value)}

    table = dynamodb.Table(tableName)
    table.put_item(
        Item=serializable_data
    )

def is_serializable(value):
    try:
        # Attempt to serialize the value
        json.dumps(value)
        return True
    except TypeError:
        # TypeError indicates the value is not serializable
        return False

class TaskType(DjangoObjectType):
    class Meta:
        model = Task

class Query(graphene.ObjectType):
    tasks = graphene.List(TaskType)

    def resolve_tasks(self, info):
        return Task.objects.all()

class CreateTask(graphene.Mutation):
    task = graphene.Field(TaskType)

    class Arguments:
        task_name = graphene.String(required=True)
        next_task_id = graphene.String()
        previous_task_id = graphene.String()
    
    def mutate(self, info, task_name, next_task_id=None, previous_task_id=None):
        id =  str(uuid.uuid1())
        task = Task(task_name=task_name, next_task_id=next_task_id, previous_task_id=previous_task_id, task_id = id)
        save_to_dynamodb("Task", **task.__dict__)
        return CreateTask(task=task)


class Mutation(graphene.ObjectType):
    create_task = CreateTask.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)

