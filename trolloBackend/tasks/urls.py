from django.urls import path
from graphene_django.views import GraphQLView
from .schema import schema  # Assuming you have a schema file

urlpatterns = [
    path('graphql/', GraphQLView.as_view(graphiql=True, schema=schema), name='graphql'),
    # Add other views or URLs as needed
]
