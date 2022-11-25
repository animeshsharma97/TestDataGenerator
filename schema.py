from marshmallow import fields, Schema, validate
from .constants.source_types import SourceTypes


class GenerateDataSchema(Schema):
    source_type = fields.Str(required=True, validate=validate.OneOf(SourceTypes.list()))
    num_records = fields.Int(required=True)
    meta = fields.Dict(required=True)
