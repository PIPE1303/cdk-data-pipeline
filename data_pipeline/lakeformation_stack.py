from aws_cdk import (
    Stack, aws_lakeformation as lf, aws_iam as iam
)
from constructs import Construct

class LakeFormationStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, *,
                 glue_db_name: str, data_bucket, athena_results_bucket,
                 analyst_principal_arn: str, glue_crawler_role_arn: str, **kwargs):
        super().__init__(scope, construct_id, **kwargs)

        analyst_principal = lf.CfnPermissions.DataLakePrincipalProperty(
            data_lake_principal_identifier=analyst_principal_arn
        )
        
        glue_crawler_principal = lf.CfnPermissions.DataLakePrincipalProperty(
            data_lake_principal_identifier=glue_crawler_role_arn
        )

        lf.CfnPermissions(
            self, "LFGlueCrawlerDbPerms",
            data_lake_principal=glue_crawler_principal,
            resource=lf.CfnPermissions.ResourceProperty(
                database_resource=lf.CfnPermissions.DatabaseResourceProperty(
                    name=glue_db_name
                )
            ),
            permissions=["CREATE_TABLE", "ALTER", "DROP", "DESCRIBE"],
            permissions_with_grant_option=["CREATE_TABLE", "ALTER", "DROP", "DESCRIBE"]
        )

        lf.CfnPermissions(
            self, "LFDbPerms",
            data_lake_principal=analyst_principal,
            resource=lf.CfnPermissions.ResourceProperty(
                database_resource=lf.CfnPermissions.DatabaseResourceProperty(
                    name=glue_db_name
                )
            ),
            permissions=["DESCRIBE"],
            permissions_with_grant_option=[]
        )

