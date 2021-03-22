from django.core.validators import BaseValidator
from django.utils.deconstruct import deconstructible


@deconstructible
class MinLengthValidator(BaseValidator):
    message = 'Value "%(value)s" has length of %(show_value)d! It should be at least %(limit_value)d symbols long!'
    code = 'too_short'

    def compare(self, a, b):
        return a < b

    def clean(self, x):
        return len(x)

class MaxLengthValidator(BaseValidator):
    message = 'Value "%(value)s" has length of %(show_value)d! It should not exceed %(limit_value)d symbols!'
    code = 'too_long'

    def compare(self, a, b):
        return a > b

    def clean(self, x):
        return len(x)


class ContentValidator(BaseValidator):
    message = 'Value "%(value)s" Does not contain valid message of the task. It should be written with proper symbols!'
    code = 'invalid_symbols'

    def has_letter(self, a):
            
    def clean(self, x):
        return x



