from django.test import TestCase
from api.models import Organization
from django.db.utils import IntegrityError


class OrganizationModelTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        super(TestCase, cls)
        Organization.objects.create(login='octokit', name='Octokit', score=10)

    def test_get_organization_by_login(self):
        organization = Organization.objects.get(login='octokit')
        self.assertEquals(organization.login, 'octokit')

    def test_save_organization_with_login_existent_not_allowed(self):
        with self.assertRaises(IntegrityError):
            Organization.objects.create(login='octokit', name='Octokit', score=10)
