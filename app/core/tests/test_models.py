from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        email = "test@test.com"
        password = "testpass123"
        user = get_user_model().objects.create_user(email=email, password=password)
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        email = "test@TESt.com"
        user = get_user_model().objects.create_user(email=email, password="password123")
        self.assertEqual(user.email, email.lower())

    def test_new_user_email_validation(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(email=None, password="123345")

    def test_creating_super_user(self):
        super_user = get_user_model().objects.create_superuser(
            "test@test.com", "password1234"
        )
        self.assertTrue(super_user.is_superuser)
        self.assertTrue(super_user.is_staff)
