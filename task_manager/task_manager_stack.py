from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_apigateway as _apigateway
)
from constructs import Construct

class TaskManagerStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        random_drink_function = _lambda.Function(
            self,
            id="RandomDrinkFunctionV4",
            code=_lambda.Code.from_asset("task_manager/code"),
            handler="lambda_handler.lambda_handler",
            runtime=_lambda.Runtime.PYTHON_3_10
        )

        api = _apigateway.LambdaRestApi(
            self,
            "Endpoint",
            handler=random_drink_function,
            deploy_options=_apigateway.StageOptions(
                throttling_burst_limit=5,
                throttling_rate_limit=1,
            ),
            proxy=True
        )

        search = api.root.add_resource("search")
        search.add_method("GET")
        search.add_method("POST")

        map = api.root.add_resource("map")
        map.add_method("GET")
        map.add_method("POST")

        delete = api.root.add_resource("delete")
        delete.add_method("GET")
        delete.add_method("POST")

        # api.root.add_method("ANY")

        # Would be interesting if I could allow all possible routes here
        # in the API Gateway so I can treat them accordingly in the routes
        # in the lambda function.
        # I think it would be something like this:
        # api.root.add_resource('/*/*')