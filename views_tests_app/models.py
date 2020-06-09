from django.db import models
from django.core.exceptions import ValidationError


# Create your models here.
class SuperHero(models.Model):
    """
    Superhero info
    """
    name = models.CharField(max_length=30)
    secret_identity = models.CharField(max_length=30)
    first_appearance = models.DateField(null=True)

    def __str__(self):
        return f'{self.name}'

    def clean(self):
        if len(self.name) > 30 or len(self.secret_identity) > 30:
            raise ValidationError(
                "31 characters is the maximum length",
                code="max_length_breached"
            )
