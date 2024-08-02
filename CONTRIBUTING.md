# Contributing to AI eBook Generator

Thank you for considering contributing to our AI eBook Generator project! Your help is greatly appreciated. Please follow these guidelines to contribute to the project.

## Table of Contents

- [Contributing to AI eBook Generator](#contributing-to-ai-ebook-generator)
  - [Table of Contents](#table-of-contents)
  - [Code of Conduct](#code-of-conduct)
  - [How to Contribute](#how-to-contribute)
    - [Reporting Bugs](#reporting-bugs)
    - [Suggesting Enhancements](#suggesting-enhancements)
    - [Pull Requests](#pull-requests)
  - [Development Setup](#development-setup)
  - [Style Guides](#style-guides)
    - [Python Style Guide](#python-style-guide)
    - [Markdown Style Guide](#markdown-style-guide)
  - [License](#license)

## Code of Conduct

Please read and follow our [Code of Conduct](CODE_OF_CONDUCT.md).

## How to Contribute

### Reporting Bugs

If you find a bug, please report it by opening an issue in the GitHub repository. Please include the following details:
- A clear and descriptive title.
- A detailed description of the bug.
- Steps to reproduce the bug.
- Any error messages or screenshots.

### Suggesting Enhancements

We welcome suggestions for new features or improvements. To suggest an enhancement, please open an issue in the GitHub repository and include:
- A clear and descriptive title.
- A detailed description of the enhancement.
- Any additional context or examples.

### Pull Requests

If you would like to contribute code, please follow these steps:
1. Fork the repository.
2. Create a new branch with a descriptive name (e.g., `feature/add-new-template`).
3. Make your changes in the new branch.
4. Test your changes thoroughly.
5. Commit your changes with a clear and descriptive commit message.
6. Push your changes to your forked repository.
7. Open a pull request to the main repository.

Please ensure your pull request:
- Clearly describes the changes and why they are needed.
- References any related issues.

## Development Setup

To set up the project for development, follow these steps:

1. **Clone the repository:**
    ```sh
    git clone https://github.com/your-username/ai-ebook-generator.git
    cd ai-ebook-generator
    ```

2. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

3. **Configure API keys:**
    - Create a `config.py` file in the project root directory.
    - Add your Cohere API key to the `config.py` file:
    ```python
    COHERE_API_KEY = 'your-cohere-api-key'
    ```

4. **Install wkhtmltopdf:**
    - Download and install wkhtmltopdf from [https://wkhtmltopdf.org/downloads.html](https://wkhtmltopdf.org/downloads.html).
    - Add `wkhtmltopdf` to your system PATH.

    **Windows:**
    ```sh
    set PATH=%PATH%;C:\Program Files\wkhtmltopdf\bin
    ```

    **macOS/Linux:**
    ```sh
    export PATH=$PATH:/usr/local/bin/wkhtmltopdf
    ```

## Style Guides

### Python Style Guide

- Follow PEP 8 guidelines.
- Use meaningful variable and function names.
- Write docstrings for all public modules, functions, classes, and methods.

### Markdown Style Guide

- Use `#` for top-level headings, `##` for second-level, and so on.
- Use `-` or `*` for unordered lists.
- Use backticks for inline code and triple backticks for code blocks.

## License

By contributing to this project, you agree that your contributions will be licensed under the project's MIT License.

Thank you for contributing!
