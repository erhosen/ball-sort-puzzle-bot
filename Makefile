clean:
	@rm -rf .coverage coverage.xml htmlcov report.xml
	@find . -type d -name '__pycache__' -exec rm -rf {} +
	@find . -type d -name '*pytest_cache*' -exec rm -rf {} +
	@find . -type f -name "*.py[co]" -exec rm -rf {} +

format:
	@pre-commit run --all-files

test:
	@python -m pytest --cov=app/ app/tests/ --durations=0 -vvv

generate_requirements:
	@poetry export --without-hashes -f requirements.txt > app/requirements.txt

check_requirements: generate_requirements
	@git diff --quiet app/requirements.txt

deploy: clean generate_requirements
	@yc serverless function version create --function-name=ball-sort-puzzle-bot --runtime python311 --entrypoint main.handler --memory 256m --execution-timeout 120s --source-path app

run:
	@yc serverless function invoke ball-sort-puzzle-bot
