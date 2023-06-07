"""
Author: Savana Rohit
Date: June 4, 2023
Description: This Python program retrieves GitHub pull request summaries within a date range.
"""

from datetime import datetime, timedelta
import os
from dotenv import load_dotenv
from github import Github
from tabulate import tabulate

# Environment variables loading
load_dotenv()

# GitHub API
github_api_key = os.getenv("GITHUB_API_KEY")

# GitHub connection instance
g = Github(github_api_key, timeout=20)

# GitHub Repo name
repo = g.get_repo("facebook/react")

# Time Period of a week
end_date = datetime.now()
start_date = end_date - timedelta(days=7)

# Last Week's Pull requests
pulls = repo.get_pulls(state="all", sort="created", base="main")
pulls_last_week = [pull for pull in pulls if start_date <= pull.created_at <= end_date]

# Pull requests summary format
pulls_data = []
for pull in pulls_last_week:
    pulls_data.append([pull.number, pull.title, pull.state])

# Pull request summary table
table = tabulate(pulls_data, headers=["Number", "Title", "State"], tablefmt="grid")

# Count of pull requests by state
counts = {"open": 0, "closed": 0, "merged": 0}

for pull in pulls_last_week:
    state = pull.state.lower()
    if state in counts:
        counts[state] += 1
        counts["merged"] += 1
        counts["open"] += 1
        counts["closed"] += 1

# Summary table with counts
summary = tabulate(counts.items(), headers=["State", "Count"], tablefmt="grid")

# Email details
From = input("Enter your email address (From):")
To = input("Enter the recipient's email address (To):")
Subject = "GitHub Pull Request Summary"

# Email Summary body
body = f"""
Dear Manager,

Here is the summary of pull requests in the last week for the facebook/react repository:

Summary:
{summary}

Complete Table
{table}

Best regards,
Your Name
"""

print("From", From)
print("To", To)
print("Subject", Subject)
print("Body", body)
