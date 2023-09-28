""" Tests for models
"""
from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):
    """Test models"""

    def test_create_user_with_email_succesful(self):
        """Test creating a user with an email is succesful"""
        # Arrange
        email = "test@example.com"
        password = "testpass123"
        # Act
        user = get_user_model().objects.create_user(  # type: ignore
            email=email,
            password=password
        )
        # Assert
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test email is normalized for new users."""
        # Arrange
        sample_emails = [
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['Test2@EXAMPLE.com', 'Test2@example.com'],
            ['TEST3@EXAMPLE.com', 'TEST3@example.com'],
            ['test4@EXAMPLE.COM', 'test4@example.com']
        ]
        # Act
        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, 'sample123')
            # Assert
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raises_error(self):
        """A user without an email raises ValueError"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'test123')

    def test_create_superuser(self):
        """Test creating a superuser"""
        # Arrange
        # Act
        user = get_user_model().objects.create_superuser(
            email="test@example.com",
            password="test1234"
        )
        # Assert
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
