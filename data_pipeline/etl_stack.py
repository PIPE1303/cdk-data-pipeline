from aws_cdk import (
    Stack, Duration, aws_iam as iam, aws_lambda as _lambda
)
from constructs import Construct

class EtlStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, *, data_bucket, lambda_role, **kwargs):
        super().__init__(scope, construct_id, **kwargs)

        self.extract_lambda = _lambda.Function(
            self, "ExtractPublicApi",
            runtime=_lambda.Runtime.PYTHON_3_12,
            handler="app.handler",
            code=_lambda.Code.from_asset("lambda_src/extractor"),
            timeout=Duration.seconds(60),
            role=lambda_role,
            environment=dict(
                DATA_BUCKET_NAME=data_bucket.bucket_name,
                API_URL="https://randomuser.me/api/?results=100"
            ),
        )

        data_bucket.grant_put(self.extract_lambda)
        data_bucket.grant_put_acl(self.extract_lambda)

        self.extract_lambda.add_to_role_policy(iam.PolicyStatement(
            actions=["s3:PutObject"],
            resources=[f"{data_bucket.bucket_arn}/*"],
        ))
