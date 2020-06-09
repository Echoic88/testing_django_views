from django.test import TestCase
from django.shortcuts import reverse
# from django.core.exceptions import ValidationError
# from django.contrib import messages
from .models import SuperHero
from .forms import SuperHeroForm


# Create your tests here.
class TestIndexView(TestCase):
    """
    Tests views
    """
    def setUp(self):
        self.form_data = {
            "name": "Wolverine",
            "secret_identity": "James Howlett",
            "first_appearance": "1974-11-01"
        }

    def test_index_displays_correct_template(self):
        response = self.client.get("/")
        form = response.context["form"]
        self.assertTemplateUsed(response, "views_tests_app/index.html")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(form, SuperHeroForm)

    def test_form_saves_to_model_correctly(self):
        response = self.client.post("/", self.form_data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, reverse("views_tests_app:index"))

        hero = SuperHero.objects.get(name="Wolverine")

        self.assertIsInstance(hero, SuperHero)
        self.assertEqual(hero.name, self.form_data["name"])
        self.assertEqual(
            hero.secret_identity, self.form_data["secret_identity"]
        )
        self.assertEqual(
            str(hero.first_appearance), self.form_data["first_appearance"]
        )

    # def test_return_error_message_if_form_is_invalid(self):
    #     self.form_data["name"] = "x"*31
    #     response = self.client.post("/", self.form_data)
    #     self.assertRaises(ValidationError)
    #     self.assert()
