"""
Tests for models.
"""
from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from core.models import (
    Company,
    LinkedBank,
    # BankAccount,
    # Transaction,
    # Application,
    # Subscription,
    # Tag,
)


def create_user():
    user = get_user_model().objects.create_user(
        email='test@example.com',
        password='testpass123'
    )
    return user


class ModelTests(TestCase):
    """Test models."""

    def setUp(self):
        self.client = Client()

    # USER

    def test_create_user_with_email_successful(self):
        """ Test creating a user with an email is successful,
            and hashed password is correct.
        """
        email = 'test@example.com'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password), password)

    def test_new_user_email_normalized(self):
        """Test email is normalized for new users."""
        # domains must be lowercase
        sample_emails = [
            ('test1@EXAMPLE.com', 'test1@example.com'),
            ('Test2@Example.com', 'Test2@example.com'),
            ('TEST3@EXAMPLE.com', 'TEST3@example.com'),
            ('test4@example.COM', 'test4@example.com'),
        ]
        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, 'sample123')

            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raises_error(self):
        """Test that creating a user without an email raises a ValueError."""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'test1234')

    def test_create_superuser(self):
        """Test creating a superuser."""
        user = get_user_model().objects.create_superuser(
            'test@example.com',
            'test12',
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)


    # COMPANY

    def test_create_company_successful(self):
        """Test creating a company is successful."""
        name = 'test_company'
        domain = 'example.com'
        company = Company.objects.create(name=name, domain=domain)

        self.assertEqual(company.name, name)
        self.assertEqual(company.domain, domain)


    # LINKED_BANK

    def test_create_linked_bank_successful(self):
        """Test creating a linked bank account (plaid item) is successful
        and that the bank's web portal is active.
        """
        name = 'test_linked_bank'
        web_portal_url = 'https://www.example.com'
        response = self.client.get(web_portal_url)

        linked_bank = LinkedBank.objects.create(
            name=name,
            web_portal_url=web_portal_url,
        )

        self.assertEqual(linked_bank.name, name)
        self.assertEqual(linked_bank.web_portal_url, web_portal_url)
        self.assertGreaterEqual(response.status_code, 200)
        self.assertLess(response.status_code, 300)

    # BANK_ACCOUNT

    # TRANSACTION

    # APPLICATION

    # SUBSCRIPTION

    # TAG
