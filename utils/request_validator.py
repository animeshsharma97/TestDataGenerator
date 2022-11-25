from functools import wraps


def request_validator(request_body, validation_schema):
    schema = validation_schema()
    errors = schema.validate(request_body)
    return errors