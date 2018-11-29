"""
radiomanager.models.types
=========================

Custom SQLAlchemy data types
"""

import uuid
from sqlalchemy.types import BINARY, TypeDecorator


class UUID(TypeDecorator):
    """
    UUID SQLAlchemy type adapter. Based on https://docs.sqlalchemy.org/en/rel_0_9/core/custom_types.html?highlight=guid#backend-agnostic-guid-type
    """
    impl = BINARY

    def load_dialect_impl(self, dialect):
        return dialect.type_descriptor(BINARY(16))

    def process_bind_param(self, value, dialect):
        if value is None:
            return None
        if isinstance(value, bytes):
            return value
        elif isinstance(value, str):
            return uuid.UUID(hex=value).bytes
        elif isinstance(value, uuid.UUID):
            return value.bytes
        else:
            raise TypeError("Unable to convert %s to uuid.UUID" %
                            (type(value),))

    def process_result_value(self, value, dialect):
        if value is None:
            return None
        return uuid.UUID(bytes=value)
