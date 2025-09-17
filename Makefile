SHELL := /bin/bash

bootstrap:
	cdk bootstrap

deploy:
	cdk deploy --all --require-approval never

destroy:
	cdk destroy --all

invoke:
	aws lambda invoke --function-name EtlStack-ExtractPublicApi69E90A74-UX9VFz9F1X19 out.json && cat out.json

crawl:
	aws glue start-crawler --name randomuser-crawler

athena-console:
	@echo "Abre Athena y usa el workgroup 'analytics'."
