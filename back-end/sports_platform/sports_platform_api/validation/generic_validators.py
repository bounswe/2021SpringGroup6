from django.core.validators import RegexValidator


english_dot = RegexValidator(r'^[a-zA-Z\.]*$', 'Only English characters and . are allowed.') 
date = RegexValidator(r'\d\d/\d\d/\d\d\d\d', 'The dates should be DD/MM/YYYY format.')
gender = RegexValidator('^male$|^female$|^decline_to_report$', 'The gender could be male, female or decline_to_report.')

