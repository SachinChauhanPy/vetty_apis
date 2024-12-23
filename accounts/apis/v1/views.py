from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework_api_key.models import APIKey
from rest_framework.permissions import IsAuthenticated
from rest_framework_api_key.permissions import HasAPIKey

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


@swagger_auto_schema(
    method="post",
    operation_description="Create a new API key for authentication.",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "name": openapi.Schema(
                type=openapi.TYPE_STRING,
                description=(
                    "The name associated with the API key. Defaults to 'Default Name'"
                    " if not provided."
                ),
            )
        },
        required=[],
    ),
    responses={
        201: openapi.Response(
            description="API Key Created Successfully",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "message": openapi.Schema(type=openapi.TYPE_STRING),
                    "name": openapi.Schema(type=openapi.TYPE_STRING),
                    "api_key": openapi.Schema(type=openapi.TYPE_STRING),
                },
            ),
        ),
        400: openapi.Response(description="Bad Request"),
    },
)
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_api_key(request):
    # Get the name from the request data
    name = request.data.get("name")
    if not name:
        name = "Default Name"

    # Create the API key
    _, key = APIKey.objects.create_key(name=name)

    # Return the API key to the user
    return Response(
        {
            "message": "API key created successfully",
            "name": name,
            "api_key": key,
        },
        status=status.HTTP_201_CREATED,
    )
