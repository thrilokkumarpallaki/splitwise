"""
    A Base model for all the classes
"""
from . import *


class BaseModelMixin:
    """
        A Base model for all the classes
    """

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime(timezone=True), default=func.now())
    last_modified_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())
