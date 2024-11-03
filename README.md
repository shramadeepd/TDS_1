#TDS Project 1

# GitHub Users and Repositories Data from Stockholm

- This project scrapes GitHub data to list users based in Stockholm with over 100 followers and their repositories, through GITHUB_api and pagination to capture all available data.
- The most interesting finding was the high concentration of users working on open-source projects, with an average of 5+ languages per user.
- Developers targeting users in Stockholm should focus on creating multilingual repositories, as many users contribute to projects in various languages.

## The analysis is done in the file - https://github.com/shramadeepd/TDS_1/blob/main/tds_analysis.ipynb

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

## Analysis and Findings

### 1. User Profiles and Company Affiliation
   - **High Engagement**: Many Stockholm-based GitHub users with over 100 followers are prolific open-source contributors, often managing numerous public repositories. This high level of engagement indicates a community dedicated to both personal and collaborative projects.
   - **Company Connections**: A significant portion of users are affiliated with prominent tech firms or startups in Stockholm. Notably, users employed at larger firms often have repositories showcasing diverse technologies, reflecting Stockholm’s innovative tech environment.

### 2. Repository Characteristics
   - **Diversity of Programming Languages**: Analysis shows that many repositories are created using a variety of programming languages. JavaScript, Python, and Java were especially prevalent, which suggests a strong emphasis on cross-language collaboration and multi-functional projects within Stockholm’s developer community.
   - **Open-source Orientation**: The presence of multiple stars and watchers across repositories indicates active public interest and participation. The high engagement levels in open-source projects reflect a robust culture of shared knowledge and code collaboration among Stockholm developers.

### 3. Licensing Trends
   - **License Preferences**: A majority of repositories are licensed under MIT, GPL, and Apache licenses, which are commonly chosen for open-source projects. This suggests that Stockholm developers prioritize flexible licensing that encourages code reuse and adaptation in collaborative environments.

## Recommendations for Developers

- **Support for Multilingual Projects**: Given the widespread use of multiple programming languages, tools or libraries that seamlessly integrate across languages would likely appeal to this community.
- **Enhanced Collaboration Features**: Stockholm developers demonstrate high engagement with collaborative open-source projects. Platforms or tools that support teamwork, project management, and community contribution tracking would benefit these users.
- **Focus on Open-Source Licensing**: The preference for permissive licenses like MIT and GPL highlights a community that values code sharing. Developers creating tools for this audience should consider options that facilitate open-source contributions and licensing flexibility.

## Instructions ( for those who run the files )

1. Ensure you have a GitHub personal access token for authenticated API requests.
2. Use the provided `fetch.py` script to fetch the data, ensuring the token is correctly added in the script.
3. Run the script to generate `users.csv` and `repositories.csv`.

## Conclusion

This analysis highlights the collaborative, multilingual, and open-source-focused nature of Stockholm's GitHub community. Developers looking to engage this group can benefit by focusing on tools that enhance multilingual support, foster teamwork, and offer flexible open-source licensing.
