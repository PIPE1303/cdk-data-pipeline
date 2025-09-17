#!/usr/bin/env python3
import os
import aws_cdk as cdk

from data_pipeline.iam_stack import IamStack
from data_pipeline.storage_stack import StorageStack
from data_pipeline.etl_stack import EtlStack
from data_pipeline.glue_stack import GlueStack
from data_pipeline.athena_stack import AthenaStack
from data_pipeline.lakeformation_stack import LakeFormationStack

app = cdk.App()

env = cdk.Environment(
    account=os.getenv("CDK_DEFAULT_ACCOUNT"),
    region=os.getenv("CDK_DEFAULT_REGION", "us-east-1"),
)

iam = IamStack(app, "IamStack", env=env)
storage = StorageStack(app, "StorageStack", env=env)

etl = EtlStack(
    app, "EtlStack",
    data_bucket=storage.data_bucket,
    lambda_role=iam.lambda_role,
    env=env
)

glue = GlueStack(
    app, "GlueStack",
    data_bucket=storage.data_bucket,
    glue_crawler_role=iam.glue_crawler_role,
    env=env
)

athena = AthenaStack(
    app, "AthenaStack",
    results_bucket=storage.results_bucket,
    env=env
)

lf = LakeFormationStack(
    app, "LakeFormationStack",
    glue_db_name=glue.db_name,
    data_bucket=storage.data_bucket,
    athena_results_bucket=storage.results_bucket,
    analyst_principal_arn=iam.analyst_role.role_arn,
    glue_crawler_role_arn=iam.glue_crawler_role.role_arn,
    env=env
)

app.synth()
