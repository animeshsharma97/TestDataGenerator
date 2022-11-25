import json
import traceback

from flask import request, jsonify, make_response
from flask.views import MethodView

from .utils.logging import log_request, log_custom_errors, get_error_response_object
from .utils.request_validator import request_validator
from .schema import GenerateDataSchema
from .handler import GenerateDataHandler


class GenerateDataView(MethodView):
    
    def post(self):
        """API to generate data.
        Returns:
            NoContent HttpResponse.
        """

        try:
            log_request(request)
            data = json.loads(request.get_data())

            errors = request_validator(data, validation_schema=GenerateDataSchema)
            if errors:
                response = {"error": errors}
                log_custom_errors(response)
                return make_response(jsonify(response), 400)

            response, response_code = GenerateDataHandler().generate_data(data)
            log_custom_errors(response, response_code)
            return make_response(jsonify(response), response_code)

        except Exception:
            response = get_error_response_object(traceback.format_exc())
            return make_response(jsonify(response), 500)
