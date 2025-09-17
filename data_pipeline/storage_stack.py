from aws_cdk import (
    Stack, RemovalPolicy, Duration, aws_s3 as s3
)
from constructs import Construct

class StorageStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs):
        super().__init__(scope, construct_id, **kwargs)

        self.data_bucket = s3.Bucket(
            self, "DataLakeRaw",
            versioned=True,
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
            encryption=s3.BucketEncryption.S3_MANAGED,
            lifecycle_rules=[s3.LifecycleRule(
                noncurrent_version_expiration=Duration.days(30)
            )],
            removal_policy=RemovalPolicy.DESTROY,
            auto_delete_objects=True,
        )

        self.results_bucket = s3.Bucket(
            self, "AthenaResults",
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
            encryption=s3.BucketEncryption.S3_MANAGED,
            removal_policy=RemovalPolicy.DESTROY,
            auto_delete_objects=True,
        )
