# Contributing to OpenSight Pro

Thank you for your interest in contributing to OpenSight Pro! We welcome contributions from the community.

## Code of Conduct

We are committed to providing a welcoming and inspiring community for all. Please read and follow our Code of Conduct.

## How to Contribute

### Reporting Bugs

Before creating bug reports, please check the issue list as you might find out that you don't need to create one. When you are creating a bug report, please include as many details as possible:

- **Use a clear and descriptive title**
- **Describe the exact steps which reproduce the problem**
- **Provide specific examples to demonstrate the steps**
- **Describe the behavior you observed after following the steps**
- **Explain which behavior you expected to see instead and why**
- **Include screenshots and animated GIFs if possible**
- **Include your environment details** (OS, Python version, etc.)

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, please include:

- **Use a clear and descriptive title**
- **Provide a step-by-step description of the suggested enhancement**
- **Provide specific examples to demonstrate the steps**
- **Describe the current behavior and expected behavior**
- **Explain why this enhancement would be useful**

### Pull Requests

- Fill in the required template
- Follow the Python styleguides
- Include appropriate test cases
- Update documentation as needed
- End all files with a newline

## Development Setup

```bash
# Clone the repository
git clone https://github.com/udhofarhanahmed/opensight.git
cd opensight

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
pytest tests/

# Format code
black src/

# Lint code
flake8 src/
```

## Styleguides

### Python Code Style

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/)
- Use [Black](https://github.com/psf/black) for code formatting
- Use [Flake8](https://flake8.pycqa.org/) for linting
- Maximum line length: 100 characters
- Use type hints where possible

### Git Commit Messages

- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit the first line to 72 characters or less
- Reference issues and pull requests liberally after the first line

Example:
```
Add support for CSV file uploads

- Implement CSV parser in data ingestion module
- Add validation for required columns
- Update documentation with CSV format requirements

Fixes #123
```

### Documentation

- Use Markdown for documentation
- Keep lines to a reasonable length (80-100 characters)
- Use clear, concise language
- Include code examples where appropriate
- Update the table of contents if adding new sections

## Testing

All contributions should include appropriate tests:

```bash
# Run all tests
pytest tests/

# Run with coverage
pytest --cov=src tests/

# Run specific test file
pytest tests/unit/test_analytics.py -v
```

## Submitting Changes

1. Fork the repository
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests and linting
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## Review Process

- At least one maintainer review is required
- All tests must pass
- Code coverage should not decrease
- Documentation should be updated

## Questions?

Feel free to open an issue or start a discussion if you have any questions!

---

Thank you for contributing to OpenSight Pro! 🎉
