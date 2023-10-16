import json
from repositories.TaskBoardRepository import TaskBoardRepository

def request_builder_middleware(event):
    """
    This middleware is responsible for building the request object

    The csv in the request body is separated from the other request data
    to simulate an environment where data would not be passed by the request, 
    but actually retrieved from some persistent storage.
    """
    body = json.loads(event["body"])
    dataset = body["dataset"]
    del body["dataset"]

    request = {
        "path": event["path"].strip("/"),
        "method": event["httpMethod"],
        "body": body
    }
    return request, dataset

def initialize_repository_middleware(csv: str):
    """
    This middleware is responsible for initializing the repository.
    
    The Repository is implemented as a singleton so that it can be initialized
    once and then used by all the controllers.

    This is being done to simulate an environment where data would not
    be passed by the request, but actually retrieved from some persistent storage.
    """
    TaskBoardRepository(csv)

def destroy_repository_middleware():
    """
    This middleware is responsible for destroying the repository.
    
    Since the lambda keeps running in the same container, the repository
    needs to be destroyed after each request so that the next request
    can re-initialize it with a different csv.
    """
    TaskBoardRepository.destroy_instance()