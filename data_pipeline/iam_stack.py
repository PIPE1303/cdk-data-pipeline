from aws_cdk import (
    Stack, CfnOutput,
    aws_iam as iam
)
from constructs import Construct

class IamStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs):
        super().__init__(scope, construct_id, **kwargs)

        self.lambda_role = iam.Role(
            self, "FullAccessLambdaRole",
            assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),
            description="Role for Lambda with full Admin access (POC only)"
        )
        self.lambda_role.add_managed_policy(
            iam.ManagedPolicy.from_aws_managed_policy_name("AdministratorAccess")
        )

        self.glue_crawler_role = iam.Role(
            self, "FullAccessGlueCrawlerRole",
            assumed_by=iam.ServicePrincipal("glue.amazonaws.com"),
            description="Role for Glue crawler with full Admin access (POC only)"
        )
        self.glue_crawler_role.add_managed_policy(
            iam.ManagedPolicy.from_aws_managed_policy_name("AdministratorAccess")
        )
        
        self.glue_crawler_role.add_to_policy(iam.PolicyStatement(
            effect=iam.Effect.ALLOW,
            actions=[
                "lakeformation:GetDataAccess",
                "lakeformation:GrantPermissions",
                "lakeformation:RevokePermissions",
                "lakeformation:ListPermissions",
                "lakeformation:GetResourceLFTags",
                "lakeformation:GetLFTag",
                "lakeformation:ListLFTags",
                "lakeformation:GetEffectivePermissionsForPath",
                "lakeformation:GetTableObjects",
                "lakeformation:GetWorkUnits",
                "lakeformation:StartQueryPlanning",
                "lakeformation:GetQueryState",
                "lakeformation:GetQueryStatistics",
                "lakeformation:StopQueryPlanning",
                "lakeformation:GetWorkUnitResults",
                "lakeformation:GetQueryResults",
                "lakeformation:GetTableObjects",
                "lakeformation:UpdateTableObjects",
                "lakeformation:DeleteTableObjects",
                "lakeformation:AddObject",
                "lakeformation:RemoveObject"
            ],
            resources=["*"]
        ))

        self.lf_admin_role = iam.Role(
            self, "FullAccessLakeFormationAdminRole",
            assumed_by=iam.AccountRootPrincipal(),
            description="LF Admin role with full Admin access (POC only)"
        )
        self.lf_admin_role.add_managed_policy(
            iam.ManagedPolicy.from_aws_managed_policy_name("AdministratorAccess")
        )

        self.analyst_role = iam.Role(
            self, "FullAccessAnalystRole",
            assumed_by=iam.AccountRootPrincipal(),
            description="Analyst role with full Admin access (POC only)"
        )
        self.analyst_role.add_managed_policy(
            iam.ManagedPolicy.from_aws_managed_policy_name("AdministratorAccess")
        )

        CfnOutput(self, "LambdaRoleArn", value=self.lambda_role.role_arn)
        CfnOutput(self, "GlueCrawlerRoleArn", value=self.glue_crawler_role.role_arn)
        CfnOutput(self, "LakeFormationAdminRoleArn", value=self.lf_admin_role.role_arn)
        CfnOutput(self, "AnalystRoleArn", value=self.analyst_role.role_arn)
