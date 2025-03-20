# ETL Most Used Languages in Github Repositories

## Overview
This project provides two ETL (Extract, Transform, Load) pipelines to interact with the GitHub API. The first pipeline extracts repository data, including the most used programming languages. The second pipeline creates a repository and uploads files programmatically.

## Prerequisites
Before running the scripts, ensure you have:

- Python 3.x installed
- Required libraries: `requests`, `pandas`, `numpy`
- A valid GitHub personal access token with repository permissions

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/ETL-Github-Languages.git
   cd ETL-Github-Languages
   ```
2. Install dependencies:
   ```bash
   pip install requests pandas numpy
   ```

---
## Pipeline 1: Extracting Most Used Languages from a GitHub User's Repositories

### Description
This script extracts repository names and their associated languages from a given GitHub user, then processes the data to identify the most used languages.

### Usage
1. Open `etl_github_languages.py` and replace the placeholder values with your GitHub username and token:
   ```python
   amazon_repo = ETLGithubRepositorys('your_github_username', 'your_github_token')
   ```
2. Run the script:
   ```bash
   python etl_github_languages.py
   ```
3. Expected Output:
   - Prints a DataFrame with the count of languages used across the repositories.
   - Saves the extracted data to a CSV file (if modified to do so).

---
## Pipeline 2: Creating a Repository and Uploading a File

### Description
This script allows users to create a private GitHub repository and upload a file to it programmatically.

### Usage
1. Open `create_github_repository.py` and replace the placeholder values:
   ```python
   repo_manager = CreateRepositoryFile(
       username='your_github_username',
       reponame='your_new_repo_name',
       archive_path='path/to/your/file.ext',
       token='your_github_token',
       private=True
   )
   ```
2. Run the script:
   ```bash
   python create_github_repository.py
   ```
3. Expected Output:
   - Prints the repository creation response.
   - Uploads the file to the repository and prints the response.

---
## Notes
- Ensure your GitHub token has the correct scopes (`repo` for private repositories).
- If working with a large number of repositories, consider implementing rate limit handling.
- Modify the scripts to save outputs to CSV for further analysis.
