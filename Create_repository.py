import base64
import requests

class CreateRepositoryFile:
    def __init__(self, username, reponame, archive_path, token, private: bool):
        """
        Initializes the class with the username, repository name, local file path, and authentication token.
        """
        self.username = username
        self.reponame = reponame
        self.archive_path = archive_path
        self.token = token
        self.private = private
        self.api_base_url = 'https://api.github.com'
        self.repo_url = f'{self.api_base_url}/repos/{self.username}/{self.reponame}'
        self.file_url = f'{self.repo_url}/contents/{self.archive_path}'
        self.headers = {
            'Authorization': f'Bearer {self.token}',
            'X-GitHub-Api-Version': '2022-11-28'
        }

    def create_private_repo(self):
        """
        Creates a private repository for the user.
        Returns the status and response data.
        """
        url = f'{self.api_base_url}/user/repos'
        payload = {
            "name": self.reponame,
            "private": self.private,
            "description": "Private repository created via API"
        }
        response = requests.post(url, headers=self.headers, json=payload)
        # If the creation is successful, update the repository and file URL.
        if response.status_code in [200, 201]:
            # Update URLs if the repository is successfully created.
            self.repo_url = f'{self.api_base_url}/repos/{self.username}/{self.reponame}'
            self.file_url = f'{self.repo_url}/contents/{self.archive_path}'
        return response.status_code, response.json()

    def encode_file(self):
        """
        Reads the local file and encodes it in base64.
        """
        try:
            with open(self.archive_path, 'rb') as file:
                encoded_content = base64.b64encode(file.read()).decode('utf-8')
            return encoded_content
        except Exception as e:
            raise Exception(f'Error reading or encoding the file: {e}')

    def config_repository(self):
        """
        Configures the data for file upload.
        """
        encoded_content = self.encode_file()
        data = {
            'message': 'Adding a new file',
            'content': encoded_content
            # Optional: 'branch': 'main', 'committer': {'name': 'Your Name', 'email': 'your_email@example.com'}
        }
        return data

    def put_file(self):
        """
        Uploads the file to the repository.
        Returns the status and response data.
        """
        data = self.config_repository()
        response = requests.put(self.file_url, headers=self.headers, json=data)
        if response.status_code in [200, 201]:
            return response.status_code, response.json()
        else:
            return response.status_code, response.json()


# Example usage:
# Replace 'your_username', 'repo_name', 'path/to/your/file.ext', and 'your_token' with actual values.

repo_manager = CreateRepositoryFile(
    username='adibhosn',
    reponame='test',
    archive_path='test.txt',
    token='kesaedçvcnasodi',
    private=True
)

# 1. Create the private repository
status_repo, response_repo = repo_manager.create_private_repo()
print("Repository creation:", status_repo, response_repo)

# 2. Upload the file
status_file, response_file = repo_manager.put_file()
print("File upload:", status_file, response_file)
