#TDS Project 1

# GitHub Users and Repositories Data from Stockholm

- This project scrapes GitHub data to list users based in Stockholm with over 100 followers and their repositories, through GITHUB_api and pagination to capture all available data.
- The most interesting finding was the high concentration of users working on open-source projects, with an average of 5+ languages per user.
- Developers targeting users in Stockholm should focus on creating multilingual repositories, as many users contribute to projects in various languages.

# The analysis is done in the file - https://github.com/shramadeepd/TDS_1/blob/main/tds_analysis.ipynb

## About (Extra)

This repository contains data collected using the GitHub API, listing users based in Stockholm with over 100 followers and their repositories.

## Files

- `users.csv`: Contains information about users from Stockholm with over 100 followers.
- `repositories.csv`: Contains information on the repositories of these users.


## Data Fields

**Users**
- `login`: GitHub user ID
- `name`: Full name
- `company`: Cleaned company name
- `location`: City (Stockholm)
- `email`: Email address
- `hireable`: Whether open for hiring
- `bio`: Bio
- `public_repos`: Number of public repositories
- `followers`: Number of followers
- `following`: Number following
- `created_at`: Join date

**Repositories**
- `login`: GitHub user ID of the owner
- `full_name`: Full name of the repository
- `created_at`: Creation date
- `stargazers_count`: Number of stars
- `watchers_count`: Number of watchers
- `language`: Language used
- `has_projects`: Whether projects are enabled
- `has_wiki`: Whether wiki is enabled
- `license_name`: License name
