from django.core.validators import RegexValidator


english_dot = RegexValidator(r'^[a-zA-Z][a-zA-Z\. ]*[a-zA-Z]$', 'Only English characters and . are allowed. Cannot start or end with .') 
english_dot_number = RegexValidator(r'^[a-zA-Z0-9][a-zA-Z0-9\. ]*[a-zA-Z0-9]$', 'Only English characters, numbers and . are allowed. Cannot start or end with .') 

date = RegexValidator(r'\d\d\d\d-\d\d-\d\d', 'The dates should be YYYY-MM-DD format.')
gender = RegexValidator('^male$|^female$|^decline_to_report$', 'The gender could be male, female or decline_to_report.')

password = RegexValidator(r'^[a-zA-Z0-9\._\*]*$', 'Only English characters, numbers, * and . are allowed.')