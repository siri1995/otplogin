from django.core.exceptions import ValidationError
import re



def validate_first_name(value):
    first_name = str(value)
    if not re.match("^[A-Za-z]*$", first_name):
        raise ValidationError("Enter only alphabats")
    return value

def validate_last_name(value):
    last_name = str(value)
    if not re.match("^[A-Za-z]*$", last_name):
        raise ValidationError("Enter only alphabets")
    return value

def validate_city(value):
    city = str(value)
    if not re.match("^[A-Za-z]*$", city):
        raise ValidationError("Enter only alphabets")
    return value

def validate_state(value):
    state = str(value)
    if not re.match("^[A-Za-z]*$", state):
        raise ValidationError("Enter only alphabets")
    return value

def validate_landmark(value):
    landmark = str(value)
    if not re.match("^[A-Za-z]*$", landmark):
        raise ValidationError("Enter only alphabets")
    return value

def validate_mobile_number(value):
    mobile_number = str(value)
    if not re.match("^[0-9]*$", mobile_number):
        raise ValidationError("Enter a Valid mobile_no")
    return value

def validate_phone_number(value):
    phone_no = str(value)
    if not re.match("^[0-9]*$", phone_no):
        raise ValidationError("Enter a Valid phone_number")
    return value