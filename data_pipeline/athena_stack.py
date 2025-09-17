from aws_cdk import (
    Stack, aws_athena as athena
)
from constructs import Construct

class AthenaStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, *, results_bucket, **kwargs):
        super().__init__(scope, construct_id, **kwargs)

        self.workgroup = athena.CfnWorkGroup(
            self, "AthenaWG",
            name="analytics",
            work_group_configuration=athena.CfnWorkGroup.WorkGroupConfigurationProperty(
                result_configuration=athena.CfnWorkGroup.ResultConfigurationProperty(
                    output_location=f"s3://{results_bucket.bucket_name}/athena-results/"
                ),
                enforce_work_group_configuration=True
            ),
            state="ENABLED"
        )
