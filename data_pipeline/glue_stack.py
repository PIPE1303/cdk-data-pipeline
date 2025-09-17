from aws_cdk import (
    Stack, aws_glue as glue, aws_iam as iam
)
from constructs import Construct

class GlueStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, *, data_bucket, glue_crawler_role, **kwargs):
        super().__init__(scope, construct_id, **kwargs)

        self.db_name = "randomuser_db"

        self.database = glue.CfnDatabase(
            self, "GlueDatabase",
            catalog_id=self.account,
            database_input=glue.CfnDatabase.DatabaseInputProperty(
                name=self.db_name
            )
        )

        self.crawler = glue.CfnCrawler(
            self, "RandomUserCrawler",
            name="randomuser-crawler",
            role=glue_crawler_role.role_arn,
            database_name=self.db_name,
            targets=glue.CfnCrawler.TargetsProperty(
                s3_targets=[glue.CfnCrawler.S3TargetProperty(
                    path=f"s3://{data_bucket.bucket_name}/raw/randomuser/"
                )]
            ),
            schema_change_policy=glue.CfnCrawler.SchemaChangePolicyProperty(
                update_behavior="UPDATE_IN_DATABASE",
                delete_behavior="DEPRECATE_IN_DATABASE"
            ),
            configuration="""{
              "Version":1.0,
              "Grouping":{"TableLevelConfiguration":3},
              "CrawlerOutput":{"Partitions":{"AddOrUpdateBehavior":"InheritFromTable"}}
            }"""
        )
        self.crawler.add_dependency(self.database)
