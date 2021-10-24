from django.core.validators import RegexValidator

english_dot = RegexValidator(r'^[a-zA-Z\.]*$', 'Only English characters and . are allowed.')