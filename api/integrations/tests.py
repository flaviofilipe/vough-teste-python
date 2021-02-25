from django.test import TestCase
from .github import GithubApi
from django.http import Http404


class GithubTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        super(TestCase, cls)
        cls.organization_login = 'instruct-br'
        cls.organization_name = 'Instruct'

    def test_get_organization_existent_by_login(self):
        github = GithubApi()
        organization = github.get_organization(self.organization_login);
        self.assertEqual(self.organization_login, organization.get('login'))
        self.assertEqual(self.organization_name, organization.get('name'))
        self.assertGreater(organization.get('score'), 0)

    def test_get_quantity_members_in_organization_by_login(self):
        github = GithubApi()
        self.assertGreater(github.get_organization_public_members(self.organization_login), 0)

    def test_get_organization_nonexistent_by_login_must_return_None(self):
        github = GithubApi()
        with self.assertRaises(Http404):
            self.assertEqual(None, github.get_organization('Test Nonexistent'))

    def test_get_quantity_members_in_organization_nonexistent_by_login_must_return_0(self):
        github = GithubApi()
        self.assertEqual(0, github.get_organization_public_members('Test Nonexistent'))

    def test_get_quantity_repositories_in_organization_existent(self):
        github = GithubApi()
        self.assertGreater(github.get_organization_repositories(self.organization_login), 0)
