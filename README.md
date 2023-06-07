# GitHub Pull Request Summary

Author: Savana Rohit
Date: June 4, 2023 
Description: This Python program retrieves GitHub pull request summaries within a date range.

## Prerequisites

- Python 3.x
- Required Python packages:
    - `dotenv`
    - `github`
    - `tabulate`

## Installation

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

## Usage

1. Run the Python program:

    python code.py

2. Follow the prompts and enter the required information:

    Your email address (From)
    The recipient's email address (To)

3. Review the generated summary and table of pull requests.

## Example Output

From Rohit-s@xyz.com

To ScrumMaster@xyz.com

Subject GitHub Pull Request Summary

Dear Manager,

Here is the summary of pull requests in the last week for the facebook/react repository:

Summary:
+---------+---------+
| State   |   Count |
+=========+=========+
| open    |      29 |
+---------+---------+
| closed  |      16 |
+---------+---------+
| merged  |      15 |
+---------+---------+

Complete Table
+----------+------------------------------------------------------------+---------+     
|   Number | Title                                                      | State   |     
+==========+============================================================+=========+
|    26883 | Add a warning to useEffect if no deps                      | open    |
+----------+------------------------------------------------------------+---------+
|    26887 | chore[devtools]: upgrade to webpack v5                     | open    |
+----------+------------------------------------------------------------+---------+
|    26888 | Fix:- Fixed dev tools inspect mode on Shadow dom           | open    |
+----------+------------------------------------------------------------+---------+
|    26889 | [Flight] Add bundler-less version of RSC using plain ESM   | closed  |
+----------+------------------------------------------------------------+---------+
|    26891 | Update ReactHooks.js                                       | open    |
+----------+------------------------------------------------------------+---------+
|    26892 | Added Filter to allow skip re-render in context consumers  | open    |
+----------+------------------------------------------------------------+---------+
|    26893 | Add test for re-mounting layout effects when re-suspending | open    |
+----------+------------------------------------------------------------+---------+
|    26894 | I run bundle.js successfully                               | open    |
+----------+------------------------------------------------------------+---------+
|    26896 | Delete processStringChunk                                  | open    |
+----------+------------------------------------------------------------+---------+
|    26898 | Funix/my branch                                            | open    |
+----------+------------------------------------------------------------+---------+
|    26900 | Concurrent fixed                                           | open    |
+----------+------------------------------------------------------------+---------+
|    26904 | Eslint fixed                                               | open    |
+----------+------------------------------------------------------------+---------+
|    26905 | Warn when a hook call is an OptionalCallExpression         | open    |
+----------+------------------------------------------------------------+---------+
|    26907 | chore: fix typo in a comment                               | open    |
+----------+------------------------------------------------------------+---------+
|    26909 | Expiration fixed                                           | open    |
+----------+------------------------------------------------------------+---------+

Best regards,
Your Name