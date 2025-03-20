import requests
import pandas as pd
import numpy as np

class ETLGithubRepositorys:
    def __init__(self, owner, token):
        """
        Initializes the class with the repository owner and authentication token.
        """
        self.owner = owner
        self.token = token
        self.api_base_url = 'https://api.github.com'
        self.url = f'{self.api_base_url}/users/{self.owner}/repos'
        self.data = None
        self.headers = {'Authorization': f'Bearer {self.token}', 'X-GitHub-Api-Version': '2022-11-28'}
        
    def request(self):
        """
        Performs pagination to collect the user's repositories.
        """
        if self.data is None:
            repo_list = []
            for page in range(1, 20):
                try:
                    params = {'page': page}
                    response = requests.get(self.url, headers=self.headers, params=params)
                    repo_list.append(response.json())
                except Exception as e:
                    raise Exception('Request error') from e
            self.data = repo_list
        return self.data

    def get_repos_names(self):
        """
        Returns a list with the names of the repositories.
        """
        name_repos_list = []
        for page in self.data:
                for repo in page:
                    name_repos_list.append(repo['name'])
        return name_repos_list

    def get_langs(self):
        """
        Returns a list with the languages of the repositories.
        """
        langs_list = []
        for page in self.data:
                for repo in page:
                    langs_list.append(repo['language'])
        return langs_list
    
    def return_df_repo_name_and_language(self):
        """
        Returns a DataFrame with the names of the repositories and their languages.
        """
        langs_list = self.get_langs()
        languages = np.array(langs_list)  # NumPy array with languages

        languages_cleaned = ['None' if lang is None else lang for lang in languages]  # Transform None to 'None'

        df = pd.DataFrame({'name': self.get_repos_names(), 'language': languages_cleaned})  # Transform the array into a DataFrame

        df_names_and_langs_cleaned = df[df['language'] != 'None']  # Remove the 'None' language
        return df_names_and_langs_cleaned
    
    def return_df_counting_the_languages(self):
        """
        Returns a DataFrame with the count of each language.
        """
        langs_list = self.get_langs()
        languages = np.array(langs_list)  # NumPy array with languages
        languages_cleaned = ['None' if lang is None else lang for lang in languages]  # Transform None to 'None'

        counts = np.unique(languages_cleaned, return_counts=True)  # Counts the number of occurrences of each language

        df_counts = pd.DataFrame({'language': counts[0], 'count': counts[1]})  # Transform the array into a DataFrame
        
        df_language_counts_cleaned = df_counts[df_counts['language'] != 'None']  # Remove the 'None' language
        return df_language_counts_cleaned.sort_values(by='count', ascending=False)
    
    def save_df_to_csv(self, df, filename):
        """
        Saves a DataFrame to a CSV file.
        """
        df.to_csv(filename, index=False)
                  
# Example usage:
amazon_repo = ETLGithubRepositorys('amzn', 'çowvwonwenldksanf')
amazon_repo.request()
print(amazon_repo.return_df_counting_the_languages())
amazon_repo.save_df_to_csv(amazon_repo.return_df_counting_the_languages(), 'languages_amazon.csv')