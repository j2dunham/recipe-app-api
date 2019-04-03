from django.test import TestCase
from django.contrib.auth import get_user_model
from core import models


def sample_user(email="test@madefor.dev", password="passtest"):
    return get_user_model().objects.create_user(email, password)


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

    def test_tag_str(self):
        tag = models.Tag.objects.create(user=sample_user(), name="Vegan")
        self.assertEqual(str(tag), tag.name)

    def test_ingredient_str(self):
        ingredient = models.Ingredient.objects.create(
            user=sample_user(), name="Cucumber"
        )
        self.assertEqual(str(ingredient), ingredient.name)

    def test_recipe_str(self):
        recipe = models.Recipe.objects.create(
            user=sample_user(),
            title="Grilled Cheese",
            time_minutes=2,
            price=3.00
        )
        self.assertEqual(str(recipe), recipe.title)