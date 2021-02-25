import os
import requests
import api.exceptions as exceptions
from django.http import Http404


class GithubApi:
    API_URL = os.environ.get("GITHUB_API_URL", "https://api.github.com")
    GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
    HEADERS = {'Authorization': f'token {GITHUB_TOKEN}'}

    def __init__(self):
        if self.GITHUB_TOKEN is None:
            raise exceptions.InvalidTokenException('Invalid Token')

    def get_organization(self, login: str):
        """Busca uma organização no Github

        :login: login da organização no Github
        """

        response = requests.get(f'{self.API_URL}/orgs/{login}', headers=self.HEADERS)
        organization = response.json()

        if response.status_code == 403 and 'limit exceeded' in organization.get('message'):
            raise exceptions.RateLimitExceededException('Limit Exceeded')

        if response.status_code == 404:
            raise Http404

        if response.status_code != 200:
            return response.json()

        data = {
            "login": organization.get('login'),
            "name": organization.get('name'),
            "score": self.get_score(login)
        }

        return data

    def get_organization_public_members(self, login: str) -> int:
        """Retorna todos os membros públicos de uma organização

        :login: login da organização no Github
        """

        response = requests.get(f'{self.API_URL}/orgs/{login}/public_members', headers=self.HEADERS)

        if response.status_code == 404:
            return 0

        return len(response.json())

    def get_organization_repositories(self, login: str) -> int:
        """Retorna todos os repositórios de uma organização

        :login: login da organização no Github
        """

        response = requests.get(f'{self.API_URL}/orgs/{login}/repos', headers=self.HEADERS)

        if response.status_code == 404:
            return 0

        return len(response.json())

    def get_score(self, login: str):
        return self.get_organization_public_members(login) + self.get_organization_repositories(login)
