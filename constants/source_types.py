from enum import Enum

class SourceTypes(Enum):
    MY_SQL = 'MY_SQL'
    POSTGRES = 'POSTGRES'

    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))

    @classmethod
    def value_of(cls, value):
        for k, v in cls.__members__.items():
            if k == value:
                return v
        else:
            raise ValueError(f"'{cls.__name__}' enum not found for '{value}'")
    