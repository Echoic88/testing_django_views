from django.test import TestCase
from .models import SuperHero
from .forms import SuperHeroForm

# Create your tests here.
class TestSuperHeroForm(TestCase):
    """
    Tests SuperHeroForm
    """
    def setUp(self):
        self.form_data = {
            "name":"Wolverine",
            "secret_identity":"James Howlett",
            "first_appearance":"1974-11-01"
        }

    def test_form_saves_with_expected_valid_data(self):
        form = SuperHeroForm(data=self.form_data)
        form.save()
        test_hero = SuperHero.objects.get(name="Wolverine")
        self.assertIsInstance(test_hero, SuperHero)
        self.assertEqual(test_hero.name, "Wolverine")
        self.assertEqual(test_hero.secret_identity, "James Howlett")
        self.assertEqual(test_hero.first_appearance, "1974-11-01")
