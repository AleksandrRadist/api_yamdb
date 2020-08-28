from django.core.validators import ValidationError
from django.utils.translation import gettext_lazy as _


def score_limits_validator(value):
    if not 1 <= value <= 10:
        raise ValidationError(
            _('%(value)s out of range from 1 to 10'),
            params={'value': value}
        )
