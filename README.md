# CDK Data Pipeline

A complete AWS data pipeline built with AWS CDK (Cloud Development Kit) that demonstrates modern data engineering practices including ETL processes, data cataloging, and analytics.

## 🏗️ Architecture

This project implements a serverless data pipeline with the following components:

```
API Data Source → Lambda (ETL) → S3 Data Lake → Glue Crawler → Glue Catalog → Athena (Analytics)
```

### Components

- **Lambda Function**: Extracts data from public APIs and stores it in S3
- **S3 Buckets**: Raw data storage and Athena query results
- **Glue Crawler**: Automatically discovers and catalogs data schemas
- **Glue Database**: Centralized data catalog
- **Athena Workgroup**: SQL analytics engine with custom configuration
- **Lake Formation**: Data governance and access control
- **IAM Roles**: Secure access management

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- Node.js 18+
- AWS CLI configured with appropriate permissions
- AWS CDK CLI installed

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/cdk-data-pipeline.git
   cd cdk-data-pipeline
   ```

2. **Set up Python environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Install CDK CLI**:
   ```bash
   npm install -g aws-cdk
   ```

4. **Bootstrap CDK** (first time only):
   ```bash
   cdk bootstrap
   ```

5. **Deploy the infrastructure**:
   ```bash
   cdk deploy --all
   ```

## 📋 Usage

### Running the Pipeline

1. **Extract data** (Lambda function):
   ```bash
   make invoke
   ```

2. **Discover schema** (Glue Crawler):
   ```bash
   make crawl
   ```

3. **Query data** (Athena):
   - Open AWS Athena console
   - Select workgroup: `analytics`
   - Use database: `randomuser_db`
   - Query table: `randomuser`

### Example Queries

```sql
-- Count total users
SELECT COUNT(*) as total_users 
FROM randomuser_db.randomuser;

-- Users by country
SELECT location.country, COUNT(*) as users_count
FROM randomuser_db.randomuser 
GROUP BY location.country 
ORDER BY users_count DESC 
LIMIT 10;

-- Sample user data
SELECT name.first, name.last, email, location.country 
FROM randomuser_db.randomuser 
LIMIT 5;
```

## 🛠️ Development

### Project Structure

```
cdk-data-pipeline/
├── app.py                          # CDK app entry point
├── requirements.txt                # Python dependencies
├── cdk.json                       # CDK configuration
├── Makefile                       # Build and deployment commands
├── data_pipeline/                 # CDK stacks
│   ├── iam_stack.py              # IAM roles and policies
│   ├── storage_stack.py          # S3 buckets
│   ├── etl_stack.py              # Lambda ETL function
│   ├── glue_stack.py             # Glue database and crawler
│   ├── athena_stack.py           # Athena workgroup
│   └── lakeformation_stack.py    # Data governance
└── lambda_src/extractor/          # Lambda function code
    ├── app.py                    # Lambda handler
    └── requirements.txt          # Lambda dependencies
```

### Available Commands

```bash
# Deploy all stacks
make deploy

# Destroy all resources
make destroy

# Invoke Lambda function
make invoke

# Start Glue crawler
make crawl

# Open Athena console (instructions)
make athena-console
```

### Environment Variables

Set these environment variables before deployment:

```bash
export CDK_DEFAULT_ACCOUNT=your-aws-account-id
export CDK_DEFAULT_REGION=us-east-1
```

## 🔧 Configuration

### Customizing Data Sources

To use a different API endpoint, modify the `API_URL` environment variable in `data_pipeline/etl_stack.py`:

```python
environment=dict(
    DATA_BUCKET_NAME=data_bucket.bucket_name,
    API_URL="https://your-api-endpoint.com/data"  # Change this
),
```

### Adjusting Crawler Configuration

Modify the crawler settings in `data_pipeline/glue_stack.py`:

```python
configuration="""{
  "Version":1.0,
  "Grouping":{"TableLevelConfiguration":3},
  "CrawlerOutput":{"Partitions":{"AddOrUpdateBehavior":"InheritFromTable"}}
}"""
```

## 🔐 Security

This project uses IAM roles with broad permissions for demonstration purposes. In production:

1. **Implement least privilege access**
2. **Use specific IAM policies** instead of AdministratorAccess
3. **Enable CloudTrail** for audit logging
4. **Use AWS Secrets Manager** for sensitive data
5. **Implement VPC endpoints** for private connectivity

## 💰 Cost Estimation

Approximate daily costs (us-east-1):

- **Lambda**: ~$0.0001 (100 executions)
- **S3**: ~$0.01 (1GB storage)
- **Glue Crawler**: ~$0.05 (1 execution)
- **Athena**: ~$0.02 (10 queries)
- **Total**: ~$0.08/day

## 🧪 Testing

### Manual Testing

1. **Deploy the stack**:
   ```bash
   cdk deploy --all
   ```

2. **Run the pipeline**:
   ```bash
   make invoke
   make crawl
   ```

3. **Verify in AWS Console**:
   - Check S3 buckets for data
   - Verify Glue table creation
   - Test Athena queries

### Automated Testing

```bash
# Synthesize CloudFormation templates
cdk synth

# Run CDK tests (if available)
pytest
```

## 🤝 Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Troubleshooting

### Common Issues

1. **CDK Bootstrap Required**:
   ```bash
   cdk bootstrap
   ```

2. **Permission Denied**:
   - Ensure AWS CLI is configured
   - Check IAM permissions
   - Verify account and region settings

3. **Lambda Timeout**:
   - Increase timeout in `etl_stack.py`
   - Check API endpoint availability

4. **Glue Crawler Fails**:
   - Verify S3 data exists
   - Check IAM role permissions
   - Review CloudWatch logs

### Getting Help

- Check AWS CloudFormation console for stack events
- Review CloudWatch logs for Lambda and Glue
- Consult AWS documentation for service-specific issues

## 🔄 Roadmap

- [ ] Add data validation and quality checks
- [ ] Implement automated scheduling with EventBridge
- [ ] Add data transformation capabilities
- [ ] Support for multiple data sources
- [ ] Implement data lineage tracking
- [ ] Add monitoring and alerting

## 📚 Resources

- [AWS CDK Documentation](https://docs.aws.amazon.com/cdk/)
- [AWS Glue Documentation](https://docs.aws.amazon.com/glue/)
- [AWS Athena Documentation](https://docs.aws.amazon.com/athena/)
- [AWS Lake Formation Documentation](https://docs.aws.amazon.com/lake-formation/)