import os
import requests


class GithubApi:
    API_URL = os.environ.get("GITHUB_API_URL", "https://api.github.com")
    GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
    HEADERS = {'Authorization': GITHUB_TOKEN}

    def get_organization(self, login: str):
        """Busca uma organização no Github

        :login: login da organização no Github
        """

        response = requests.get(f'{self.API_URL}/orgs/{login}', headers=self.HEADERS)

        if response.status_code == 404:
            return None

        return response.json()

    def get_organization_public_members(self, login: str) -> int:
        """Retorna todos os membros públicos de uma organização

        :login: login da organização no Github
        """

        response = requests.get(f'{self.API_URL}/orgs/{login}/public_members', headers=self.HEADERS)

        if response.status_code == 404:
            return 0

        return len(response.json())
