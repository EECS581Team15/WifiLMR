"""
radiomanager.models.device
==========================

Device-specific database models.
"""

from .. import FlaskExtensions
from ..models import types


class Device(FlaskExtensions.db.Model):
    __db = FlaskExtensions.db
    internal_id = __db.Column(__db.Integer, primary_key=True)
    public_key = __db.Column(__db.BLOB)
    name = __db.Column(__db.String)
    uuid = __db.Column(types.UUID, unique=True, nullable=False)
    key_revoked = __db.Column(__db.Boolean, default=False)
