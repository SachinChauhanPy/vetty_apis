import requests

from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_api_key.permissions import HasAPIKey
from rest_framework.decorators import api_view, permission_classes

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from decouple import config

gecko_base_url = config(
    "GECKO_URL", default="https://pro-api.coingecko.com/api/v3/")


@swagger_auto_schema(
    method="get",
    operation_description="Fetch a paginated list of all coins including their IDs.",
    manual_parameters=[
        openapi.Parameter(
            "page_num",
            openapi.IN_QUERY,
            description="Page number for pagination",
            type=openapi.TYPE_INTEGER,
            default=1,
        ),
        openapi.Parameter(
            "per_page",
            openapi.IN_QUERY,
            description="Number of items per page",
            type=openapi.TYPE_INTEGER,
            default=10,
        ),
    ],
    responses={
        200: openapi.Response(
            description="Success",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "results": openapi.Schema(
                        type=openapi.TYPE_ARRAY,
                        items=openapi.Items(type=openapi.TYPE_OBJECT),
                    ),
                    "page_num": openapi.Schema(type=openapi.TYPE_INTEGER),
                    "per_page": openapi.Schema(type=openapi.TYPE_INTEGER),
                    "total_records": openapi.Schema(type=openapi.TYPE_INTEGER),
                },
            ),
        ),
        500: openapi.Response(description="Internal Server Error"),
    },
)
@api_view(["GET"])
@permission_classes([IsAuthenticated | HasAPIKey])
def coin_list_view(request):
    """
    Fetch a paginated list of all coins including their IDs.
    """
    # Define the correct endpoint URL
    url = f"{gecko_base_url}coins/list"

    try:
        # Fetch data from the CoinGecko API
        response = requests.get(url, timeout=5)

        # Raise an exception for HTTP errors
        response.raise_for_status()
        data = response.json()

        # Manual pagination
        page_num = int(request.query_params.get("page_num", 1))
        per_page = int(request.query_params.get("per_page", 10))
        start = (page_num - 1) * per_page
        end = start + per_page
        paginated_data = data[start:end]

        return Response(
            {
                "results": paginated_data,
                "page_num": page_num,
                "per_page": per_page,
                "total_records": len(data),
            }
        )

    except requests.exceptions.RequestException as e:
        return Response({"error": f"Failed to fetch coin data: {str(e)}"}, status=500)


@swagger_auto_schema(
    method="get",
    operation_description="Fetch a paginated list of coin categories.",
    manual_parameters=[
        openapi.Parameter(
            "page_num",
            openapi.IN_QUERY,
            description="Page number for pagination",
            type=openapi.TYPE_INTEGER,
            default=1,
        ),
        openapi.Parameter(
            "per_page",
            openapi.IN_QUERY,
            description="Number of items per page",
            type=openapi.TYPE_INTEGER,
            default=10,
        ),
    ],
    responses={
        200: openapi.Response(
            description="Success",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "results": openapi.Schema(
                        type=openapi.TYPE_ARRAY,
                        items=openapi.Items(type=openapi.TYPE_OBJECT),
                    ),
                    "page_num": openapi.Schema(type=openapi.TYPE_INTEGER),
                    "per_page": openapi.Schema(type=openapi.TYPE_INTEGER),
                    "total": openapi.Schema(type=openapi.TYPE_INTEGER),
                },
            ),
        ),
        500: openapi.Response(description="Internal Server Error"),
    },
)
@api_view(["GET"])
@permission_classes([IsAuthenticated | HasAPIKey])
def coin_categories_view(request):
    """
    Fetch a paginated list of coin categories.
    """
    # Correct URL for fetching coin categories
    url = f"{gecko_base_url}coins/categories/list"

    try:
        # Fetch data from CoinGecko API
        response = requests.get(url, timeout=5)

        # Raise an exception for HTTP errors
        response.raise_for_status()
        data = response.json()

        # Manual pagination
        page_num = int(request.query_params.get("page_num", 1))
        per_page = int(request.query_params.get("per_page", 10))
        start = (page_num - 1) * per_page
        end = start + per_page
        paginated_data = data[start:end]

        return Response(
            {
                "results": paginated_data,
                "page_num": page_num,
                "per_page": per_page,
                "total": len(data),
            }
        )

    except requests.exceptions.RequestException as e:
        return Response(
            {"error": f"Failed to fetch coin categories: {str(e)}"}, status=500
        )


@swagger_auto_schema(
    method="get",
    operation_description="Fetch market data for a specific coin by its ID, filtered by CAD.",
    manual_parameters=[],
    responses={
        200: openapi.Response(
            description="Success",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "id": openapi.Schema(type=openapi.TYPE_STRING),
                    "symbol": openapi.Schema(type=openapi.TYPE_STRING),
                    "name": openapi.Schema(type=openapi.TYPE_STRING),
                    "market_data": openapi.Schema(type=openapi.TYPE_OBJECT),
                },
            ),
        ),
        404: openapi.Response(description="Coin not found"),
        500: openapi.Response(description="Internal Server Error"),
    },
)
@api_view(["GET"])
@permission_classes([IsAuthenticated | HasAPIKey])
def specific_coin_view(request, coin_id):
    """
    Fetch market data for a specific coin by its ID, filtered by CAD.
    """
    # Correct URL for fetching specific coin market data
    url = f"{gecko_base_url}coins/markets"
    params = {
        "vs_currency": "cad",  # Filter market data by CAD
        "ids": coin_id,  # Fetch specific coin by ID
    }

    try:
        # Fetch data from CoinGecko API
        # Add timeout for safety
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()

        if data:
            # Return the first (and only) item for the requested coin ID
            return Response(data[0])
        else:
            # No data found for the given coin_id
            return Response(
                {"error": f"No data found for coin ID: {coin_id}"}, status=404
            )

    except requests.exceptions.RequestException as e:
        return Response({"error": f"Failed to fetch coin data: {str(e)}"}, status=500)


@swagger_auto_schema(
    method="get",
    operation_description="Check the health of the CoinGecko API.",
    responses={
        200: openapi.Response(
            description="Healthy",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "status": openapi.Schema(
                        type=openapi.TYPE_STRING, description="Health status"
                    ),
                    "message": openapi.Schema(
                        type=openapi.TYPE_STRING,
                        description="Details of the API health",
                    ),
                },
            ),
        ),
        500: openapi.Response(description="Unhealthy"),
    },
)
@api_view(["GET"])
@permission_classes([IsAuthenticated | HasAPIKey])
def check_gecko_api_health(request):
    """
    API to check the health of the CoinGecko API.
    Returns a JSON response with status and message.
    """
    url = f"{gecko_base_url}ping"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return Response(
                {"status": "healthy", "message": "CoinGecko API is accessible."}
            )
        return Response(
            {
                "status": "unhealthy",
                "message": f"CoinGecko API returned status code {response.status_code}.",
            },
            status=500,
        )
    except requests.RequestException as e:
        return Response(
            {
                "status": "unhealthy",
                "message": f"Error accessing CoinGecko API: {str(e)}",
            },
            status=500,
        )
