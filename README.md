## GitHub Pull Request Summary

Author: Savana Rohit <br>
Date: June 4, 2023 <br>
Description: This Python code retrieves GitHub pull request summaries within a date range. <br>

### Prerequisites

- Python 3.9
- Required Python packages:
    - `datetime`
    - `github`
    - `python-dotenv`
    - `PyGithub`
    - `tabulate`

### Installation

1. Clone the repository:

    git clone https://github.com/your-username/your-repo.git

2. Change into the project directory:

    cd your-repo

3. Install the required packages:

    pip install -r requirements.txt

4. Set up the environment variables:

    Create a .env file in the project directory.

    Add the following line to the .env file:

    GITHUB_API_KEY=your-github-api-key

    Replace your-github-api-key with your personal GitHub API key.

### Usage

1. Run the Python program:

    python code.py

2. Follow the prompts and enter the required information:

    Your email address (From)
    The recipient's email address (To)

3. Review the generated summary and table of pull requests.

