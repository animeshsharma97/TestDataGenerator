import logging
import os
import traceback


logger = logging.getLogger()


def log_request(request):
    logger.info(vars(request))


def log_custom_errors(response, response_code=400):
    if int(response_code / 100) != 2:
        logger.warning(response)


def get_error_response_object(exception=None, message=None):
    response = {
        "error": {
            "message": exception or message or "Something went wrong",
            "code": 500,
        }
    }
    logger.error({"error": exception})
    return response
