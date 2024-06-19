"""
Tests for models.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from core.models import (
    Company,
    
)


class ModelTests(TestCase):
    """Test models."""

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

    # BANK_ACCOUNT

    # TRANSACTION

    # APPLICATION

    # SUBSCRIPTION

    # TAG
