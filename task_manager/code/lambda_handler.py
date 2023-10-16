import json
from routes import ROUTES
from utils.middlewares import request_builder_middleware, initialize_repository_middleware

def lambda_handler(event, context):
    """
    This is the entrypoint for the lambda function.
    The event parameter is a dictionary containing the request information.
    The context parameter is a dictionary containing the AWS context information.

    Here we are delegating the request validation responsability to the controllers
    in order to keep request specific information transparent to the handler.
    This way the lambda_handler doesn't need to be updated. Any new routes can be added
    to the ROUTES dictionary.
    """

    try:
        request, dataset = request_builder_middleware(event)
        initialize_repository_middleware(dataset)
        route = ROUTES[f"{request['method']} {request['path']}"]
        response = route(request)
        return response
    except KeyError:
        return {
            'statusCode': 404,
            'body': json.dumps({"message": f"Route '{request['method']} {request['path']}' not found"}),
        }
    except Exception as e:
        return {
            'statusCode': 400,
            'body': json.dumps({"message": str(e)}),
        }