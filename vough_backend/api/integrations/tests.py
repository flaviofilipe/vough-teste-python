from django.test import TestCase
from .github import GithubApi


class GithubTestCase(TestCase):
    def test_get_organization_existent_by_login(self):
        github = GithubApi()
        self.assertEqual('octokit', github.get_organization('octokit').get('login'))

    def test_get_quantity_members_in_organization_by_login(self):
        github = GithubApi()
        self.assertEqual(11, github.get_organization_public_members('octokit'))

    def test_get_organization_nonexistent_by_login_must_return_None(self):
        github = GithubApi()
        self.assertEqual(None, github.get_organization('Test Nonexistent'))

    def test_get_quantity_members_in_organization_nonexistent_by_login_must_return_0(self):
        github = GithubApi()
        self.assertEqual(0, github.get_organization_public_members('Test Nonexistent'))
