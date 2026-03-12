import re
from rest_framework import status
from rest_framework.exceptions import ValidationError

email_regex = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
phone_regex = re.compile(r'^998([378][2]|(9[013-57-9]))\d{7}$')

def check_email_or_phone(user_input):
    if re.fullmatch(phone_regex, user_input):
        return 'phone'
    elif re.fullmatch(email_regex, user_input):
        return 'email'
    else:
        raise ValidationError({
            "status": False,
            "message": "Email yoki telefon raqami noto'g'ri kiritildi."
        })
