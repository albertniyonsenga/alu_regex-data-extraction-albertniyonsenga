# Here will import all functions to be used in validation 
from .Emails import validate_email
from .Urls import validate_url
from .Phone_numbers import validate_phone
from .Currency import validate_currency
from .tags import validate_hashtags
from .time_formats import validate_time_12, validate_time_24

VALIDATORS = {
    'email': validate_email,
    'url': validate_url,
    'phone': validate_phone,
    'currency': validate_currency,
    'hashtags': validate_hashtags,
    'time (12-hour format)': validate_time_12,
    'time (24-hour format)':validate_time_24 
}