# Contributing to CDK Data Pipeline

Thank you for your interest in contributing to this project! This document provides guidelines for contributing to the CDK Data Pipeline.

## Getting Started

1. Fork the repository
2. Clone your fork locally
3. Create a new branch for your feature or bugfix
4. Make your changes
5. Test your changes
6. Submit a pull request

## Development Setup

### Prerequisites

- Python 3.11+
- Node.js 18+
- AWS CLI configured
- AWS CDK CLI installed

### Setup

1. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt
   ```

3. Install CDK CLI:
   ```bash
   npm install -g aws-cdk
   ```

4. Bootstrap CDK (first time only):
   ```bash
   cdk bootstrap
   ```

## Code Style

- Follow PEP 8 for Python code
- Use meaningful variable and function names
- Add docstrings for functions and classes
- Keep functions small and focused

## Testing

Before submitting a pull request:

1. Run the CDK synth command to ensure templates are valid:
   ```bash
   cdk synth
   ```

2. Test the deployment in a development environment:
   ```bash
   cdk deploy --all
   ```

3. Verify the pipeline works end-to-end:
   ```bash
   make invoke
   make crawl
   ```

## Pull Request Process

1. Ensure your code follows the project's style guidelines
2. Add tests if applicable
3. Update documentation if needed
4. Ensure all tests pass
5. Submit a pull request with a clear description of changes

## Issues

When reporting issues, please include:

- Description of the problem
- Steps to reproduce
- Expected behavior
- Actual behavior
- Environment details (OS, Python version, etc.)

## License

By contributing to this project, you agree that your contributions will be licensed under the MIT License.
