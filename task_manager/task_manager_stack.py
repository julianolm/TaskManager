from aws_cdk import core as cdk
# from aws_cdk import Stack
# from constructs import Construct
from aws_cdk import aws_lambda

class TaskManagerStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        random_drink_function = aws_lambda.Function(
            self,
            id="RandomDrinkFunctionV2",
            code=aws_lambda.Code.from_asset("task_manager\compute"),
            handler="first_function.lambda_handler",
            runtime=aws_lambda.Runtime.PYTHON_3_11
        )