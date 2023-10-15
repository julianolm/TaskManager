import json
from .controllers import search_controller, map_controller, delete_controller

controllers = {
    "": lambda event, context: "You've accessed the root route",
    "search": search_controller,
    "map": map_controller,
    "delete": delete_controller
}

def lambda_handler(event, context):
    request_info = {"path": event["path"], "req_method": event["httpMethod"], "req_body": event["body"]}
    response = {}
    
    route = event["path"].strip("/").split("/")

    controller = controllers.get(route[0], None)
    if controller:
        response["body"] = controller(event, context)
    else:
        response["body"] = "no controller found"
    
    return {
        'statusCode': 200,
        'body': json.dumps({"request_info": request_info, "response": response}),
    }