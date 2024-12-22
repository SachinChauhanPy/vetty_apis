from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework_api_key.models import APIKey
from rest_framework.permissions import IsAuthenticated

from rest_framework_api_key.permissions import HasAPIKey


@api_view(['POST'])
@permission_classes([IsAuthenticated | HasAPIKey])
def create_api_key(request):
    # Get the name from the request data
    name = request.data.get("name")
    if not name:
        name = 'Default Name'

    # Create the API key
    api_key, key = APIKey.objects.create_key(name=name)

    # Return the API key to the user
    return Response({
        "message": "API key created successfully",
        "name": name,
        "api_key": key,
    }, status=status.HTTP_201_CREATED)