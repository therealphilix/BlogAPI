from django.core.validators import RegexValidator
import re

phone_regex = RegexValidator(
    regex=r'^\+?1?\d{9,15}$',
    message= 'Enter a valid phone number in the format"+829399484"'
)