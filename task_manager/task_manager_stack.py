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
            code=_lambda.Code.from_asset("task_manager\lambda_handler"),
            handler="first_function.lambda_handler",
            runtime=_lambda.Runtime.PYTHON_3_10
        )

        _apigateway.LambdaRestApi(
            self,
            "Endpoint",
            handler=random_drink_function,
            deploy_options=_apigateway.StageOptions(
                throttling_burst_limit=5,
                throttling_rate_limit=1
            ),
        )