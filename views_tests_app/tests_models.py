from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import SuperHero

# Create your tests here.
class TestSuperHeroModel(TestCase):
    def setUp(self):
        self.hero = SuperHero.objects.create(
            name="Wolverine",
            secret_identity="James Howlett",
            first_appearance="1974-11-01"
        )

    def test_model_is_valid_with_expected_valid_data(self):
        self.assertIsInstance(self.hero, SuperHero)

    def test_raise_validation_error_if_name_greater_than_30_characters(self):
        test_hero = self.hero
        test_hero.name = "x"*31
        with self.assertRaisesMessage(ValidationError, "31 characters is the maximum length"):
            test_hero.clean()

    def test_raise_validation_error_if_secret_identity_greater_than_30_characters(self):
        test_hero = self.hero
        test_hero.secret_identity = "x"*31
        with self.assertRaisesMessage(ValidationError, "31 characters is the maximum length"):
            test_hero.clean()

    def test_raise_first_appearance_can_be_null(self):
        test_hero = self.hero
        test_hero.first_appearance = None
        test_hero.save()
        self.assertIsInstance(test_hero, SuperHero)
        test_retrieve = SuperHero.objects.get(name="Wolverine")
        self.assertIs(test_retrieve.first_appearance, None)
        