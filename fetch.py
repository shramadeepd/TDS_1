import requests
import pandas as pd

# Your GitHub personal access token
TOKEN = 'token'

# Headers for authenticated API requests
headers = {
    'Authorization': f'token {TOKEN}',
}

# Function to fetch all pages of users based in Stockholm with more than 100 followers
def fetch_users():
    users = []
    page = 1
    while True:
        url = f'https://api.github.com/search/users?q=location:Stockholm+followers:>100&per_page=100&page={page}'
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        page_users = response.json().get('items', [])
        
        # Break if no more users are found
        if not page_users:
            break

        users.extend(page_users)
        page += 1

    return users

# Function to fetch all repositories for each user, with pagination for up to 500 repositories
def fetch_repositories(username):
    repositories = []
    page = 1
    while True:
        url = f'https://api.github.com/users/{username}/repos?per_page=100&sort=pushed&page={page}'
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        page_repos = response.json()

        # Break if no more repositories are found or 500 repos have been collected
        if not page_repos or len(repositories) >= 500:
            break

        repositories.extend(page_repos)
        page += 1

    return repositories[:500]

# Function to clean up the company name
def clean_company_name(company):
    if company:
        company = company.strip()  # Trim whitespace
        if company.startswith('@'):
            company = company[1:]  # Strip the leading @ symbol
        company = company.upper()  # Convert to uppercase
    return company

# Main function to collect data
def main():
    users_data = []
    repositories_data = []

    users = fetch_users()
    
    for user in users:
        user_details_url = user['url']
        user_response = requests.get(user_details_url, headers=headers)
        user_response.raise_for_status()
        user_details = user_response.json()
        
        # Extract and clean user information
        user_info = {
            'login': user_details['login'],
            'name': user_details.get('name', ''),
            'company': clean_company_name(user_details.get('company', '')),
            'location': user_details.get('location', ''),
            'email': user_details.get('email', ''),
            'hireable': user_details.get('hireable', ''),
            'bio': user_details.get('bio', ''),
            'public_repos': user_details.get('public_repos', 0),
            'followers': user_details.get('followers', 0),
            'following': user_details.get('following', 0),
            'created_at': user_details.get('created_at', ''),
        }
        users_data.append(user_info)

        # Fetch repositories for the user
        repos = fetch_repositories(user_details['login'])
        for repo in repos:
            repo_info = {
                'login': user_details['login'],
                'full_name': repo['full_name'],
                'created_at': repo['created_at'],
                'stargazers_count': repo['stargazers_count'],
                'watchers_count': repo['watchers_count'],
                'language': repo['language'] if repo['language'] else '',
                'has_projects': repo['has_projects'],
                'has_wiki': repo['has_wiki'],
                'license_name': repo['license']['key'] if repo['license'] else '',
            }
            repositories_data.append(repo_info)

    return users_data, repositories_data

# Execute the main function
users_data, repositories_data = main()

# Convert to DataFrames
users_df = pd.DataFrame(users_data)
repositories_df = pd.DataFrame(repositories_data)

# Save to CSV
users_df.to_csv('users.csv', index=False)
repositories_df.to_csv('repositories.csv', index=False)

print("Data has been saved to users.csv and repositories.csv")
